import card_api.core.domain.games.card as _d_card


class Player:
    def __init__(self, player_account: str, hand: list, score: int):
        self.player_account = player_account
        self.hand = hand
        self.score = score

    def draw_card(self, card: _d_card.Card):
        hand = [] + self.hand
        hand.append(card)
        self.hand = hand
        score = self.calculate_score()
        self.score = score
        return self

    def calculate_score(self):
        score = 0
        for card in self.hand:
            score += card.face.value
        return score

    @classmethod
    def new(
        cls,
        player_account: str,
    ):
        return cls(player_account=player_account, hand=[], score=0)

    @classmethod
    def to_dict(cls, player: "Player"):
        hand_list = []
        for card in player.hand:
            card_dict = {"suit": card.suit.value, "face": card.face.value}
            hand_list.append(card_dict)
        player_dict = {
            "player_account": player.player_account,
            "hand": hand_list,
            "score": player.score,
        }
        return player_dict
