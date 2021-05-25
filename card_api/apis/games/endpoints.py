import mongoengine as _me

import card_api.common.exception as _exc
import card_api.core.application as _a_game
import card_api.core.domain.games.deck as _d_deck
import card_api.core.domain.games.game as _d_game
from card_api.providers.repositories.decks import *  # noqa F403, F401
from card_api.providers.repositories.games import *  # noqa F403, F401
from card_api.providers.repositories.players import *  # noqa F403, F401
from card_api.providers.services.deck_calculator import *  # noqa F403, F401


def deck_to_json(deck: _d_deck.Deck):
    return {"deckId": str(deck.id), "deckCards": deck.cards}


def game_to_json(game: _d_game.Game):
    return {"gameId": str(game.id), "deckId": game.deck_id}


def create_game():
    game = _a_game.create_game()
    return {"gameId": str(game.id)}, 201


def delete_game(**kwargs):
    game_id = kwargs["gameId"]
    try:
        _a_game.delete_game(game_id=game_id)
    except _exc.GameDoesNotExist as e:
        return {"message": str(e)}, 404
    else:
        return game_id


def create_deck():
    deck = _a_game.create_deck()
    return deck_to_json(deck), 201


def add_deck_to_game(**kwargs):
    game_id = kwargs["gameId"]
    deck_id = kwargs["deckId"]
    try:
        game = _a_game.add_deck_to_game(game_id=game_id, deck_id=deck_id)
    except _exc.GameDoesNotExist as e:
        return {"message": str(e)}, 404
    except _exc.DeckDoesNotExist as e:
        return {"message": str(e)}, 404
    except _exc.DeckAlreadyExist as e:
        return {"message": str(e)}, 405
    else:
        return game


def add_player_to_game(**kwargs):
    game_id = kwargs["gameId"]
    player_account = kwargs["playerAccount"]
    try:
        game = _a_game.add_player_to_game(
            game_id=game_id, player_account=player_account
        )
    except _exc.GameDoesNotExist as e:
        return {"message": str(e)}, 404
    except _exc.PlayerAlreadyPartOfTheGame as e:
        return {"message": str(e)}, 409
    else:
        return game, 201


def deal_card_to_player(**kwargs):
    game_id = kwargs["gameId"]
    player_account = kwargs["playerAccount"]
    try:
        player = _a_game.deal_card_to_player(
            game_id=game_id, player_account=player_account
        )
    except _me.DoesNotExist as e:
        return {"message": str(e)}, 404
    except _exc.PlayerNotPartOfTheGame as e:
        return {"message": str(e)}, 405
    except _exc.EmptyGameDeck as e:
        return {"message": str(e)}, 405
    else:
        return player


def get_list_of_cards(**kwargs):
    game_id = kwargs["gameId"]
    player_account = kwargs["playerAccount"]
    try:
        player_hand = _a_game.get_list_of_cards(
            game_id=game_id, player_account=player_account
        )
    except _exc.GameDoesNotExist as e:
        return {"message": str(e)}, 404
    except _exc.PlayerNotPartOfTheGame as e:
        return {"message": str(e)}, 405
    else:
        return player_hand


def get_list_of_players(**kwargs):
    game_id = kwargs["gameId"]
    try:
        players_list = _a_game.get_list_of_players(game_id=game_id)
    except _exc.GameDoesNotExist as e:
        return {"message": str(e)}, 404
    else:
        return players_list


def get_list_of_undealt_suits(**kwargs):
    game_id = kwargs["gameId"]
    try:
        suits_undealt = _a_game.get_undealt_suits(game_id=game_id)
    except _exc.GameDoesNotExist as e:
        return {"message": str(e)}, 404
    else:
        return suits_undealt


def count_undealt_cards(**kwargs):
    game_id = kwargs["gameId"]
    try:
        ordered_cards_list = _a_game.get_card_count(game_id=game_id)
    except _exc.GameDoesNotExist as e:
        return {"message": str(e)}, 404
    else:
        return ordered_cards_list


def shuffle(**kwargs):
    game_id = kwargs["gameId"]
    try:
        game = _a_game.shuffle_game_deck(game_id=game_id)
    except _exc.GameDoesNotExist as e:
        return {"message": str(e)}, 404
    else:
        return game
