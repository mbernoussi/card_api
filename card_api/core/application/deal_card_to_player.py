import antidote as _antidote
import card_api.core.application.interfaces as _interfaces
import card_api.core.domain.games.game as _d_game
import card_api.common.exception as _exc


@_antidote.inject
def deal_card_to_player(
    player_repo: _interfaces.PlayersRepository,
    game_repo: _interfaces.GamesRepository,
    deck_repo: _interfaces.DecksRepository,
    game_id: str,
    player_account: str,
) -> _d_game.Game:
    player = player_repo.find_by_id(player_account)
    game = game_repo.find_by_id(game_id)
    if player.player_account not in game.players:
        raise _exc.PlayerNotAddedToGane()
    game_decks = game.decks
    if game.decks == []:
        raise _exc.EmptyGameDeck()
    current_deck_id = game_decks[0]
    current_deck = deck_repo.find_by_id(current_deck_id)
    card_dealt = current_deck.deal_card()
    player = player.draw_card(card_dealt)
    player_repo.save(player)
    deck_repo.save(current_deck)
    if len(current_deck.cards) == 0:
        game_decks_modified = [] + game_decks
        game_decks_modified.remove(current_deck_id)
        game.decks = game_decks_modified
        game_repo.save(game)
    return player
