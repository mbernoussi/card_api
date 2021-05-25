import antidote as _antidote
import mongoengine as _me

import card_api.core.application as _a_game
import card_api.core.domain.games.card as _d_card
import card_api.core.domain.games.deck as _d_deck


class Deck(_me.Document):
    _id = _me.StringField(required=True, primary_key=True)
    cards = _me.ListField()

    @classmethod
    def from_entity(cls, deck: _d_deck.Deck) -> "Deck":
        cards_list = []
        for card in deck.cards:
            cards_list.append(
                {"suit": card.suit.value, "face": card.face.value}
            )
        return cls(_id=str(deck.id), cards=cards_list)

    def to_entity(self) -> _d_deck.Deck:
        cards = []
        for card_dict in self.cards:
            card = _d_card.Card(
                _d_card.Suit(card_dict["suit"]),
                _d_card.Face(card_dict["face"]),
            )
            cards.append(card)
        deck = _d_deck.Deck(deck_id=self._id, cards=cards)
        return deck


@_antidote.implements(_a_game.DecksRepository)
@_antidote.register
class DecksRepository(_a_game.DecksRepository):
    def save(self, deck: _d_deck.Deck):
        deck = Deck.from_entity(deck)
        deck.save()

    def delete(self, deck_id):
        Deck(_id=deck_id).delete()

    def find_by_id(self, deck_id: str) -> _d_deck.Deck:
        deck_doc = Deck.objects.get(_id=deck_id)
        deck = deck_doc.to_entity()
        return deck
