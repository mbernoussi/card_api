import antidote as _antidote
import mongoengine as _me

import card_api.core.application as _a_game
import card_api.core.domain.games.card as _d_card
import card_api.core.domain.games.player as _d_player


class Player(_me.Document):
    _id = _me.StringField(required=True, primary_key=True)
    hand = _me.ListField()
    score = _me.IntField()

    @classmethod
    def from_entity(cls, player: _d_player.Player) -> "Player":
        hand_list = []
        for card in player.hand:
            hand_list.append(
                {"suit": card.suit.value, "face": card.face.value}
            )
        return cls(
            _id=str(player.player_account), hand=hand_list, score=player.score
        )

    def to_entity(self) -> _d_player.Player:
        hand_list = []
        for card_dict in self.hand:
            hand_list.append(
                _d_card.Card(
                    _d_card.Suit(card_dict["suit"]),
                    _d_card.Face(card_dict["face"]),
                )
            )
        player = _d_player.Player(
            player_account=self._id, hand=hand_list, score=self.score
        )
        return player


@_antidote.implements(_a_game.PlayersRepository)
@_antidote.register
class PlayersRepository(_a_game.PlayersRepository):
    def save(self, player: _d_player.Player):
        player = Player.from_entity(player)
        player.save()

    def delete(self, player_account):
        Player(_id=player_account).delete()

    def find_by_id(self, player_account: str) -> _d_player.Player:
        player_doc = Player.objects.get(_id=player_account)
        player = player_doc.to_entity()
        return player
