from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re

from .errors import InvalidIdentifier


class IdKind(str, Enum):
    NETWORK = "NET"
    IDENTITY = "MID"
    RELATIONSHIP = "REL"
    ENTERPRISE = "ENT"
    CONTRIBUTION = "CTR"
    AGREEMENT = "AGR"
    ATTESTATION = "ATT"
    EVENT = "EVT"


_PATTERN = re.compile(r"^(NET|MID|REL|ENT|CTR|AGR|ATT|EVT):([A-Z0-9]{2,12}):([0-9]{6})$")


@dataclass(frozen=True, slots=True)
class ProtocolId:
    kind: IdKind
    namespace: str
    sequence: int

    def __post_init__(self) -> None:
        if not re.fullmatch(r"[A-Z0-9]{2,12}", self.namespace):
            raise InvalidIdentifier("namespace must be 2-12 uppercase alphanumeric characters")
        if self.sequence < 1 or self.sequence > 999999:
            raise InvalidIdentifier("sequence must be between 1 and 999999")

    def __str__(self) -> str:
        return f"{self.kind.value}:{self.namespace}:{self.sequence:06d}"


def make_id(kind: IdKind, namespace: str, sequence: int) -> str:
    return str(ProtocolId(kind=kind, namespace=namespace, sequence=sequence))


def parse_id(value: str, expected_kind: IdKind | None = None) -> ProtocolId:
    match = _PATTERN.fullmatch(value)
    if not match:
        raise InvalidIdentifier(f"invalid protocol id: {value!r}")
    parsed = ProtocolId(IdKind(match.group(1)), match.group(2), int(match.group(3)))
    if expected_kind is not None and parsed.kind is not expected_kind:
        raise InvalidIdentifier(f"expected {expected_kind.value} id, got {parsed.kind.value}")
    return parsed
