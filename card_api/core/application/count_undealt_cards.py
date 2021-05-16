import antidote as _antidote
import card_api.core.application.interfaces as _interfaces


@_antidote.inject
def get_undealt_suits(
    game_repo: _interfaces.GamesRepository,
    deck_repo: _interfaces.DecksRepository,
    deck_calcultor: _interfaces.DeckCalculator,
    game_id: str,
) -> list:
    game = game_repo.find_by_id(game_id)
    game_deck = game.decks
    undealt_cards = deck_calcultor.count_undealt_cards(game_deck)
    return undealt_cards
