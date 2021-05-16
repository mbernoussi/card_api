import antidote as _antidote
import card_api.core.application as _a_game
import card_api.providers.repositories.decks as _r_deck


@_antidote.implements(_a_game.DeckCalculator)
@_antidote.register
class DeckCalculatorService(_a_game.DeckCalculator):
    @_antidote.inject
    def calculate_undealt(self, game_deck, deck_repo: _r_deck.DecksRepository) -> dict:
        undealt_cards_by_suit = {}
        spade_sum = 0
        diamond_sum = 0
        heart_sum = 0
        club_sum = 0
        for deck_id in game_deck:
            deck = deck_repo.find_by_id(deck_id)
            spade_sum += sum(
                card.__dict__.get("suit").value == "SPADE" for card in deck.cards
            )
            diamond_sum += sum(
                card.__dict__.get("suit").value == "DIAMOND" for card in deck.cards
            )
            heart_sum += sum(
                card.__dict__.get("suit").value == "HEART" for card in deck.cards
            )
            club_sum += sum(
                card.__dict__.get("suit").value == "CLUB" for card in deck.cards
            )
        undealt_cards_by_suit["SPADE"] = spade_sum
        undealt_cards_by_suit["DIAMOND"] = diamond_sum
        undealt_cards_by_suit["HEART"] = heart_sum
        undealt_cards_by_suit["CLUB"] = club_sum
        return undealt_cards_by_suit
