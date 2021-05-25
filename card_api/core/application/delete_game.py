import antidote as _antidote

import card_api.core.application.interfaces as _interfaces
import card_api.core.domain.games.game as _d_game
from card_api.common.exception import GameDoesNotExist


@_antidote.inject
def delete_game(
    game_repo: _interfaces.GamesRepository, game_id: str
) -> _d_game.Game:
    try:
        game = game_repo.find_by_id(game_id)
    except Exception:
        raise GameDoesNotExist
    game_repo.delete(game.id)
    return game_id
