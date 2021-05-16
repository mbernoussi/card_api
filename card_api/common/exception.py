"""Module for exceptions"""


class PlayerDoesNotExist(Exception):
    def __init__(self):
        super().__init__("The player doesn't exist")


class PlayerNotAddedToGane(Exception):
    def __init__(self):
        super().__init__("The player needs to be added to the game")


class EmptyGameDeck(Exception):
    def __init__(self):
        super().__init__("The Game deck is empty")


class GameDoesNotExist(Exception):
    def __init__(self):
        super().__init__("The game doesn't exist")


class DeckDoesNotExist(Exception):
    def __init__(self):
        super().__init__("The deck doesn't exist")


class DeckAlreadyExist(Exception):
    def __init__(self):
        super().__init__("The deck already exist")


class PlayerAlreadyPartOfTheGame(Exception):
    def __init__(self):
        super().__init__("The player is already part of the game")


class PlayerNotPartOfTheGame(Exception):
    def __init__(self):
        super().__init__("The player is not part of the game")
