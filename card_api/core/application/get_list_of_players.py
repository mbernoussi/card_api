import antidote as _antidote
import card_api.core.application.interfaces as _interfaces
import card_api.core.domain.games.player as _d_player
import card_api.common.exception as _exc


@_antidote.inject
def get_list_of_players(
    player_repo: _interfaces.PlayersRepository,
    game_repo: _interfaces.GamesRepository,
    game_id: str,
) -> list:
    try:
        game = game_repo.find_by_id(game_id)
    except Exception:
        raise _exc.GameDoesNotExist
    players_list = []
    for player in game.players:
        player_entity = player_repo.find_by_id(player)
        player_dict = _d_player.Player.to_dict(player_entity)
        players_list.append(player_dict)
    players_list_sorted = sorted(players_list, key=lambda i: i["score"], reverse=True)
    return players_list_sorted
