import card_api.core.application as _a_game
import card_api.core.domain.games.deck as _d_deck


def test_create_game(mocker):
    deck_repo = mocker.Mock()
    deck = _a_game.create_deck(repo=deck_repo)
    assert isinstance(deck, _d_deck.Deck)
