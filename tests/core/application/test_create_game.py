import card_api.core.application as _a_game
import card_api.core.domain.games.game as _d_game


class TestCreateUser:
    @staticmethod
    def test_create_game(mocker):
        game_repo = mocker.Mock()
        game = _a_game.create_game(repo=game_repo)
        assert isinstance(game, _d_game.Game)
