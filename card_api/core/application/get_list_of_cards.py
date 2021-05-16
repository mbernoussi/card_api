import antidote as _antidote
import card_api.core.application.interfaces as _interfaces
import card_api.core.domain.games.game as _d_game
import card_api.common.exception as _exc


@_antidote.inject
def get_list_of_cards(
    player_repo: _interfaces.PlayersRepository,
    game_repo: _interfaces.GamesRepository,
    game_id: str,
    player_account: str,
) -> _d_game.Game:
    try:
        game = game_repo.find_by_id(game_id)
    except Exception:
        raise _exc.GameDoesNotExist
    if player_account in game.players:
        player = player_repo.find_by_id(player_account)
        return player.hand
    else:
        raise _exc.PlayerNotPartOfTheGame
