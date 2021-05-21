test_data_count = 20
import uuid as _uuid

import card_api.core.domain.games.card as _card


def build_entity_ids():
    entity_ids_list = []
    for i in range(test_data_count):
        entity_id = str(_uuid.uuid4())
        entity_ids_list.append(entity_id)
    return entity_ids_list


games_ids_list = build_entity_ids()
decks_ids_list = build_entity_ids()
players_list = [
    "Maria",
    "Alex",
    "Sophia",
    "Christoper",
    "Ali",
    "Xiang",
    "Brian",
    "Noah",
    "Chloe",
    "Farah",
    "Tanya",
    "Michel",
    "Pierre",
    "Albert",
    "Elizabeth",
    "Ramon",
    "Alan",
    "Mostapha",
    "Bruce",
    "Jean-Claude",
]


def build_cards_by_suit(suit):
    suit_cards = []
    for face in _card.Face:
        suit_cards.append(_card.Card(suit, face))
    return suit_cards


heart_cards = build_cards_by_suit(_card.Suit.HEART)
spade_cards = build_cards_by_suit(_card.Suit.SPADE)
club_cards = build_cards_by_suit(_card.Suit.CLUB)
diamond_cards = build_cards_by_suit(_card.Suit.DIAMOND)

deck_cards = heart_cards + spade_cards + club_cards + diamond_cards
