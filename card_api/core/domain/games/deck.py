import random as _random
import uuid as _uuid

import card_api.core.domain.games.card as _card


class Deck:
    def __init__(self, deck_id: str, cards: list):
        self.id_ = deck_id
        self.cards = cards

    @property
    def id(self) -> str:
        return self.id_

    def build(self):
        for suit in _card.Suit:
            for face in _card.Face:
                self.cards.append(_card.Card(suit, face))

    def shuffle(self):
        for index in range(len(self.cards) - 1, 0, -1):
            random_index = _random.randint(0, index)
            self.cards[index], self.cards[random_index] = (
                self.cards[random_index],
                self.cards[index],
            )

    def deal_card(self):
        cards = []
        cards = [] + self.cards
        card = cards.pop()
        self.cards = cards
        return card

    @classmethod
    def new(
        cls,
    ):
        return cls(deck_id=str(_uuid.uuid4()), cards=[])
