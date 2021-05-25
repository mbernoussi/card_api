import uuid as _uuid


class Game:
    def __init__(self, game_id: str, decks: list, players: list):
        self.id_ = game_id
        self.decks = decks
        self.players = players

    @property
    def id(self) -> str:
        return self.id_

    def add_deck(self, deck_id: str):
        self.decks.append(deck_id)

    @classmethod
    def new(
        cls,
    ):
        return cls(game_id=str(_uuid.uuid4()), decks=[], players=[])
