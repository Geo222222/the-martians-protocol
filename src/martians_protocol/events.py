from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
from typing import Any, Mapping

from .errors import InvariantViolation
from .ids import IdKind, parse_id


def _canonical_json(value: Mapping[str, Any]) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _is_sha256(value: str) -> bool:
    return len(value) == 64 and all(c in "0123456789abcdef" for c in value)


@dataclass(frozen=True, slots=True)
class ProtocolEvent:
    event_id: str
    network_id: str
    event_type: str
    actor_id: str
    subject_id: str
    payload: Mapping[str, Any]
    occurred_at: datetime
    previous_event_hash: str | None = None
    payload_hash: str | None = None

    def __post_init__(self) -> None:
        parse_id(self.event_id, IdKind.EVENT)
        parse_id(self.network_id, IdKind.NETWORK)
        if parse_id(self.actor_id).kind not in {IdKind.IDENTITY, IdKind.ENTERPRISE}:
            raise InvariantViolation("event actor must be an identity or enterprise")
        parse_id(self.subject_id)
        if not self.event_type.strip():
            raise InvariantViolation("event type cannot be empty")
        if self.occurred_at.tzinfo is None:
            raise InvariantViolation("event timestamp must be timezone-aware")
        if self.previous_event_hash is not None and not _is_sha256(self.previous_event_hash):
            raise InvariantViolation("previous_event_hash must be a SHA-256 hex digest")
        computed = hashlib.sha256(_canonical_json(self.payload).encode("utf-8")).hexdigest()
        if self.payload_hash is None:
            object.__setattr__(self, "payload_hash", computed)
        elif self.payload_hash != computed:
            raise InvariantViolation("payload_hash does not match canonical payload")

    def digest(self) -> str:
        material = {
            "event_id": self.event_id,
            "network_id": self.network_id,
            "event_type": self.event_type,
            "actor_id": self.actor_id,
            "subject_id": self.subject_id,
            "payload_hash": self.payload_hash,
            "occurred_at": self.occurred_at.astimezone(timezone.utc).isoformat().replace("+00:00", "Z"),
            "previous_event_hash": self.previous_event_hash,
        }
        return hashlib.sha256(_canonical_json(material).encode("utf-8")).hexdigest()


class EventLedger:
    """Append-only per-network hash chain. This is deliberately not a blockchain."""

    def __init__(self) -> None:
        self._events: dict[str, list[ProtocolEvent]] = {}
        self._event_ids: set[str] = set()

    def append(self, event: ProtocolEvent) -> str:
        if event.event_id in self._event_ids:
            raise InvariantViolation("event ids cannot be reused")
        stream = self._events.setdefault(event.network_id, [])
        expected_previous = stream[-1].digest() if stream else None
        if event.previous_event_hash != expected_previous:
            raise InvariantViolation("event previous hash does not match network ledger head")
        stream.append(event)
        self._event_ids.add(event.event_id)
        return event.digest()

    def events(self, network_id: str) -> tuple[ProtocolEvent, ...]:
        parse_id(network_id, IdKind.NETWORK)
        return tuple(self._events.get(network_id, ()))

    def verify(self, network_id: str) -> bool:
        previous = None
        for event in self.events(network_id):
            if event.previous_event_hash != previous:
                return False
            previous = event.digest()
        return True
