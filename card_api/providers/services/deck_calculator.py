import antidote as _antidote

import card_api.core.application as _a_game
import card_api.providers.repositories.decks as _r_deck


@_antidote.implements(_a_game.DeckCalculator)
@_antidote.register
class DeckCalculatorService(_a_game.DeckCalculator):
    @_antidote.inject
    def calculate_undealt(
        self, game_deck, deck_repo: _r_deck.DecksRepository
    ) -> dict:
        undealt_cards_by_suit = {}
        spade_sum = 0
        diamond_sum = 0
        heart_sum = 0
        club_sum = 0
        for deck_id in game_deck:
            deck = deck_repo.find_by_id(deck_id)
            spade_sum += sum(
                card.__dict__.get("suit").value == "SPADE"
                for card in deck.cards
            )
            diamond_sum += sum(
                card.__dict__.get("suit").value == "DIAMOND"
                for card in deck.cards
            )
            heart_sum += sum(
                card.__dict__.get("suit").value == "HEART"
                for card in deck.cards
            )
            club_sum += sum(
                card.__dict__.get("suit").value == "CLUB"
                for card in deck.cards
            )
        undealt_cards_by_suit["SPADE"] = spade_sum
        undealt_cards_by_suit["DIAMOND"] = diamond_sum
        undealt_cards_by_suit["HEART"] = heart_sum
        undealt_cards_by_suit["CLUB"] = club_sum
        return undealt_cards_by_suit

    @_antidote.inject
    def calculate_card_count(
        self, game_deck, deck_repo: _r_deck.DecksRepository
    ):
        def define_unique_list(cards_list):
            unique_list = []
            for card in cards_list:
                if card not in unique_list:
                    unique_list.append(card)
            return unique_list

        cards_list = []
        for deck_id in game_deck:
            deck = deck_repo.find_by_id(deck_id)
            for card in deck.cards:
                cards_list.append(card)
        card_count_dict = {
            str(card): cards_list.count(card) for card in cards_list
        }
        unique_card_list = define_unique_list(cards_list)
        unique_card_list_sorted = sorted(unique_card_list, reverse=True)
        ordered_cards_list = [
            {str(card): card_count_dict[str(card)]}
            for card in unique_card_list_sorted
        ]

        return ordered_cards_list
