import card_api.core.domain.games.game as _d_game
import card_api.core.domain.games.deck as _d_deck
import card_api.core.application as _a_game
import pytest as _pytest
import card_api.common.exception as _exc


@_pytest.fixture
def game_repo(mocker):
    game_repo = mocker.Mock()
    return game_repo


@_pytest.fixture
def deck_repo(mocker):
    deck_repo = mocker.Mock()
    return deck_repo


@_pytest.fixture
def deck() -> _d_deck.Deck:
    deck = _d_deck.Deck.new()
    return deck


@_pytest.fixture
def game() -> _d_game.Game:
    game = _d_game.Game.new()
    return game


def test_add_deck_to_game(game_repo, deck_repo, deck, game):
    game_repo.find_by_id.return_value = game
    deck_repo.find_by_id.return_value = deck
    game_id = game.id
    deck_id = deck.id
    game = _a_game.add_deck_to_game(game_repo, deck_repo, game_id, deck_id)
    assert isinstance(game, _d_game.Game)
    assert deck_id in game.decks


def test_add_notfound_deck_to_game(game_repo, deck_repo, deck, game):
    game_repo.find_by_id.return_value = game
    deck_repo.find_by_id.side_effect = Exception
    game_id = game.id
    deck_id = deck.id
    with _pytest.raises(_exc.DeckDoesNotExist):
        _a_game.add_deck_to_game(game_repo, deck_repo, game_id, deck_id)


def test_add_deck_to_notfound_game(game_repo, deck_repo, deck, game):
    game_repo.find_by_id.side_effect = Exception
    deck_repo.find_by_id.return_value = deck
    game_id = game.id
    deck_id = deck.id
    with _pytest.raises(_exc.GameDoesNotExist):
        _a_game.add_deck_to_game(game_repo, deck_repo, game_id, deck_id)


def test_add_deck_already_exist_to_game(game_repo, deck_repo, deck, game):
    game_repo.find_by_id.return_value = game
    deck_repo.find_by_id.return_value = deck
    game_id = game.id
    deck_id = deck.id
    game_with_deck_added = _a_game.add_deck_to_game(
        game_repo, deck_repo, game_id, deck_id
    )
    assert deck_id in game_with_deck_added.decks
    with _pytest.raises(_exc.DeckAlreadyExist):
        _a_game.add_deck_to_game(game_repo, deck_repo, game_id, deck_id)
