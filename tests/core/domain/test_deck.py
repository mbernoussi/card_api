import random as _random

import pytest as _pytest

import card_api.core.domain.games.deck as _deck
import tests.test_data as _data

DECK_CARD_COUNT = 52


def build_decks_data():
    decks_data = []
    deck_cards = _data.deck_cards
    for i in range(_random.randint(1, _data.test_data_count)):
        deck_id = _random.choice(_data.games_ids_list)
        deck_data = (deck_id, deck_cards)
        decks_data.append(deck_data)
    return decks_data


decks_data = build_decks_data()


class TestDeck:
    @staticmethod
    @_pytest.mark.parametrize("deck_id, cards", decks_data)
    def test_init_deck(deck_id, cards):
        deck = _deck.Deck(deck_id, cards)
        assert deck.id_ == deck_id
        assert deck.cards == cards

    @staticmethod
    @_pytest.mark.parametrize("deck_id, cards", decks_data)
    def test_deck_id(deck_id, cards):
        deck = _deck.Deck(deck_id, cards)
        assert deck.id == deck_id

    @staticmethod
    def test_new_deck():
        deck = _deck.Deck.new()
        assert deck.id != ""
        assert isinstance(deck.id, str)
        assert deck.cards == []

    @staticmethod
    def test_build_deck():
        for i in range(_data.test_data_count):
            deck = _deck.Deck.new()
            deck.build()
            assert len(deck.cards) == DECK_CARD_COUNT

    @staticmethod
    def test_shuffle():
        deck = _deck.Deck.new()
        deck.build()
        assert len(deck.cards) == DECK_CARD_COUNT
        deck.shuffle()
        assert len(deck.cards) == DECK_CARD_COUNT

    @staticmethod
    def test_deal_card():
        deck_count = DECK_CARD_COUNT
        deck = _deck.Deck.new()
        deck.build()
        for i in range(DECK_CARD_COUNT):
            print(deck_count)
            deck.deal_card()
            print(len(deck.cards))
            deck_count -= 1
            assert len(deck.cards) == deck_count
