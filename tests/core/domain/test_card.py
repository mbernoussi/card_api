import random as _random

import pytest as _pytest

import card_api.core.domain.games.card as _card
import tests.test_data as _data


def build_cards_data():
    cards_data = []
    for i in range(_random.randint(1, _data.test_data_count)):
        suit = _random.choice(list(_card.Suit))
        face = _random.choice(list(_card.Face))
        player_data = (suit, face)
        cards_data.append(player_data)
    return cards_data


cards_data = build_cards_data()


class TestCard:
    @staticmethod
    @_pytest.mark.parametrize("suit, face", cards_data)
    def test_init_game(suit, face):
        card = _card.Card(suit, face)
        assert card.suit == suit
        assert card.face == face

    @staticmethod
    def test_equal_cards():
        first_card = _card.Card(_card.Suit.HEART, _card.Face.ACE)
        second_card = _card.Card(_card.Suit.HEART, _card.Face.ACE)
        assert first_card == second_card

    @staticmethod
    def test_card_comparison():
        first_card = _card.Card(_card.Suit.HEART, _card.Face.ACE)
        second_card = _card.Card(_card.Suit.SPADE, _card.Face.ACE)
        third_card = _card.Card(_card.Suit.SPADE, _card.Face.KING)
        assert second_card < first_card
        assert third_card > second_card
        assert third_card > first_card

    @staticmethod
    def test_card_string_representation():
        card = _card.Card(_card.Suit.HEART, _card.Face.JACK)
        assert str(card) == "JACK of HEART"
