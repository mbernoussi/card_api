import antidote as _antidote

import card_api.common.exception as _exc
import card_api.core.application.interfaces as _interfaces
import card_api.core.domain.games.game as _game


@_antidote.inject
def shuffle_game_deck(
    game_repo: _interfaces.GamesRepository,
    deck_repo: _interfaces.DecksRepository,
    game_id: str,
) -> _game.Game:
    try:
        game = game_repo.find_by_id(game_id)
    except Exception:
        raise _exc.GameDoesNotExist
    game_deck = game.decks
    for deck_id in game_deck:
        deck = deck_repo.find_by_id(deck_id)
        deck.shuffle()
        deck_repo.save(deck)
    return game
