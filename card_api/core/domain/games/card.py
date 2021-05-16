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


class Card:
    def __init__(self, suit: Suit, face: Face):
        self.suit = suit
        self.face = face
