from poker.game import (
    get_deck,
    shuffle_deck,
    split_deck,
    deal_cards
)


def lets_play():
    deck = get_deck()

    print("Number of cards on Deck: {}".format(len(deck)))

    shuffled_deck = shuffle_deck(times=10, deck=deck)

    print("Number of cards on Deck: {}".format(len(shuffled_deck)))

    left, right = split_deck(shuffled_deck)

    shuffled_deck = right + left

    player_1, player_2, player_3, player_4, shuffled_deck = deal_cards(shuffled_deck)

    print("Player 1: {}".format(player_1))
    print("Player 2: {}".format(player_2))
    print("Player 3: {}".format(player_3))
    print("Player 4: {}".format(player_4))
