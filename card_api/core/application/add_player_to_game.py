import antidote as _antidote

import card_api.common.exception as _exc
import card_api.core.application.interfaces as _interfaces
import card_api.core.domain.games.game as _d_game
import card_api.core.domain.games.player as _d_player


@_antidote.inject
def add_player_to_game(
    game_repo: _interfaces.GamesRepository,
    player_repo: _interfaces.PlayersRepository,
    game_id: str,
    player_account: str,
) -> _d_game.Game:
    try:
        game = game_repo.find_by_id(game_id)
    except Exception:
        raise _exc.GameDoesNotExist
    players_list = [] + game.players
    if player_account not in players_list:
        players_list.append(str(player_account))
    else:
        raise _exc.PlayerAlreadyPartOfTheGame
    game.players = players_list
    game_repo.save(game)
    player = _d_player.Player.new(player_account)
    player_repo.save(player)
    return game
