import antidote as _antidote

import card_api.common.exception as _exc
import card_api.core.application.interfaces as _interfaces


@_antidote.inject
def get_card_count(
    game_repo: _interfaces.GamesRepository,
    deck_calcultor: _interfaces.DeckCalculator,
    game_id: str,
) -> list:
    try:
        game = game_repo.find_by_id(game_id)
    except Exception:
        raise _exc.GameDoesNotExist
    game_deck = game.decks
    ordered_cards_list = deck_calcultor.calculate_card_count(game_deck)
    return ordered_cards_list
