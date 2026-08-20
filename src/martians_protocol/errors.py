class ProtocolError(Exception):
    """Base protocol-domain error."""


class InvariantViolation(ProtocolError):
    """Raised when a protocol invariant would be violated."""


class InvalidIdentifier(ProtocolError):
    """Raised when an identifier is malformed or of the wrong kind."""


class InvalidTransition(ProtocolError):
    """Raised when an object lifecycle transition is not allowed."""
