import random as _random
import uuid as _uuid

import pytest as _pytest

import card_api.core.domain.games.game as _game
import tests.test_data as _data


def build_games_data():
    players_data = []
    for i in range(_random.randint(1, _data.test_data_count)):
        game_id = _random.choice(_data.games_ids_list)
        decks_list = [
            _random.choice(_data.decks_ids_list)
            for deck in range(_random.randint(1, _data.test_data_count))
        ]
        players_list = [
            _random.choice(_data.players_list)
            for player in range(_random.randint(1, _data.test_data_count))
        ]
        player_data = (game_id, decks_list, players_list)
        players_data.append(player_data)
    return players_data


games_data = build_games_data()


class TestGame:
    @staticmethod
    @_pytest.mark.parametrize("game_id, decks, players", games_data)
    def test_init_game(game_id: str, decks: list, players: list):
        game = _game.Game(game_id, decks, players)
        assert game.id_ == game_id
        assert game.decks == decks
        assert game.players == players

    @staticmethod
    @_pytest.mark.parametrize("game_id, decks, players", games_data)
    def test_game_id_render(game_id: str, decks: list, players: list):
        game = _game.Game(game_id, decks, players)
        assert game.id == game_id

    @staticmethod
    @_pytest.mark.parametrize("game_id, decks, players", games_data)
    def test_add_deck(game_id: str, decks: list, players: list):
        game = _game.Game(game_id, decks, players)
        deck_id = _random.choice(_data.decks_ids_list)
        game.add_deck(deck_id)
        assert deck_id in game.decks

    @staticmethod
    def test_new_game():
        new_game = _game.Game.new()
        assert new_game.id_ != ""
        assert new_game.decks == []
        assert new_game.players == []
