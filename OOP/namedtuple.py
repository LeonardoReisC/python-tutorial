from typing import NamedTuple


class Card(NamedTuple):
    value: str = "VALUE"
    suit: str = "SUIT"


ace = Card("A", "♠")

print(ace.value, ace.suit)
print(ace._asdict())