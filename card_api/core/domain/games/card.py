import enum as _enum


class Face(_enum.Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Suit(_enum.Enum):
    HEART = "HEART"
    SPADE = "SPADE"
    CLUB = "CLUB"
    DIAMOND = "DIAMOND"


SUIT_RANKING = [Suit.HEART, Suit.SPADE, Suit.CLUB, Suit.DIAMOND]


class Card:
    def __init__(self, suit: Suit, face: Face):
        self.suit = suit
        self.face = face

    def __eq__(self, other: "Card") -> bool:
        return (self.face.value == other.face.value) and (
            self.suit.value == other.suit.value
        )

    def __str__(self) -> str:
        return "{} of {}".format(self.face.name, self.suit.value)

    def __lt__(self, other: "Card"):
        if self.face.value == other.face.value:
            return SUIT_RANKING.index(self.suit) > SUIT_RANKING.index(
                other.suit
            )
        else:
            return self.face.value < other.face.value
