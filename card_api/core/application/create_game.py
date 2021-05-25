import antidote as _antidote

import card_api.core.application.interfaces as _interfaces
import card_api.core.domain.games.game as _d_game


@_antidote.inject
def create_game(repo: _interfaces.GamesRepository) -> _d_game.Game:
    game = _d_game.Game.new()
    repo.save(game)
    return game
