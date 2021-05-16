import dataclasses as _dtc


@_dtc.dataclass
class DeckDTO:
    id: str
    cards: list = _dtc.field(default_factory=list)
