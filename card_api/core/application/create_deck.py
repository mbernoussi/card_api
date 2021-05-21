import antidote as _antidote

import card_api.core.application.interfaces as _interfaces
import card_api.core.domain.games.deck as _d_deck


@_antidote.inject
def create_deck(repo: _interfaces.DecksRepository) -> _d_deck.Deck:
    deck = _d_deck.Deck.new()
    deck.build()
    deck.shuffle()
    repo.save(deck)
    return deck
