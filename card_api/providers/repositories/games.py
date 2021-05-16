import antidote as _antidote
import mongoengine as _me
import card_api.core.application as _a_game
import card_api.core.domain.games.game as _d_game


class Game(_me.Document):
    _id = _me.StringField(required=True, primary_key=True)
    decks = _me.ListField()
    players = _me.ListField()


@_antidote.implements(_a_game.GamesRepository)
@_antidote.register
class GamesRepository(_a_game.GamesRepository):
    def save(self, game: _d_game.Game):
        Game(_id=str(game.id), decks=game.decks, players=game.players).save()

    def delete(self, game_id):
        Game(_id=game_id).delete()

    def find_by_id(self, game_id: str) -> _d_game.Game:
        repo_game = Game.objects.get(_id=str(game_id))
        game = _d_game.Game(
            game_id=repo_game._id, decks=repo_game.decks, players=repo_game.players
        )
        return game
