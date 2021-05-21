import antidote as _antidote

import card_api.common.exception as _exc
import card_api.core.application.interfaces as _interfaces
import card_api.core.domain.games.game as _d_game


@_antidote.inject
def add_deck_to_game(
    game_repo: _interfaces.GamesRepository,
    deck_repo: _interfaces.DecksRepository,
    game_id: str,
    deck_id: str,
) -> _d_game.Game:
    try:
        game = game_repo.find_by_id(game_id)
    except Exception:
        raise _exc.GameDoesNotExist
    try:
        deck = deck_repo.find_by_id(deck_id)
    except Exception:
        raise _exc.DeckDoesNotExist
    if deck_id in game.decks:
        raise _exc.DeckAlreadyExist
    decks_list = [] + game.decks
    decks_list.append(str(deck.id))
    game.decks = decks_list
    game_repo.save(game)
    return game
