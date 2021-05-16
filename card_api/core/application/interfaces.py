import abc as _abc
import typing as _t

import card_api.core.domain.games.game as _d_game
import card_api.core.domain.games.deck as _d_deck
import card_api.core.domain.games.player as _d_player


class GamesRepository(_abc.ABC):
    @_abc.abstractmethod
    def save(self, game: _d_game) -> None:
        raise NotImplementedError

    @_abc.abstractmethod
    def delete(self, game_id: str) -> None:
        raise NotImplementedError

    @_abc.abstractmethod
    def find_by_id(self, game_id: str) -> _d_game.Game:
        raise NotImplementedError


class DecksRepository(_abc.ABC):
    @_abc.abstractmethod
    def save(self, deck: _d_deck) -> None:
        raise NotImplementedError

    @_abc.abstractmethod
    def find_by_id(self, deck_id: str) -> _d_deck.Deck:
        raise NotImplementedError


class PlayersRepository(_abc.ABC):
    @_abc.abstractmethod
    def save(self, player: _d_player) -> None:
        raise NotImplementedError

    @_abc.abstractmethod
    def find_by_id(self, player_id: str) -> _d_player.Player:
        raise NotImplementedError


class DeckCalculator(_abc.ABC):
    @_abc.abstractmethod
    def calculate_undealt(self, game: _d_game.Game):
        raise NotImplementedError
