from random import randint

NUMBERS = [
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
]

FIGURES = [
    'H', 'D', 'C', 'S'
]


def get_deck():
    """
    Function that build up the poker deck
    Figures:
        H - Hearts
        D - Diamonds
        C - Clubs
        S - Spades
    Numbers:
        1, 2, 3, 4, 5, 6, 7, 8, 9, J, Q, K
    :return: A list of string with the following structure {NUMBER}-{FIGURE}
    """
    deck = []
    for figure in FIGURES:
        for number in NUMBERS:
            deck.append('{number}-{figure}'.format(
                figure=figure,
                number=number
            ))
    return deck


def shuffle_deck(times=1, deck=[]):
    """
    Functions that shuffle a deck n number of times
    :param times: Number of time the deck is shuffle
    :param deck: List of cards (String) to shuffle
    :return: List of card on the deck shuffle
    """

    def _take_cards(part_of_deck):
        """
        Internal function that randomly take a n number of cards from the part of the deck
        :param part_of_deck: List of cards, subset of the entire deck
        :return: Two list of cards (String), first is the taken cards, the second is the leftover of the cards
        """
        if len(part_of_deck) > 2:
            number_of_cards = randint(1, len(part_of_deck))
            taken_cards = part_of_deck[: number_of_cards]
            leftover_cards = part_of_deck[number_of_cards:]
        else:
            taken_cards = part_of_deck
            leftover_cards = []
        return taken_cards, leftover_cards

    for _ in range(times):
        shuffled_deck = []
        left, right = split_deck(deck)
        keep_going = True
        while keep_going:
            if randint(1, 10) % 2 == 1:  # Random number
                # 1 use right
                taken_cards, right = _take_cards(right)
            else:
                # 0 use left
                taken_cards, left = _take_cards(left)

            # add the taken cards to the shuffled deck
            shuffled_deck += taken_cards[:]

            # check if either side is empty
            if len(left) == 0 or len(right) == 0:
                # If any of the sides is empty stop shuffling and append the rest of the deck to the shuffled deck
                keep_going = False
                shuffled_deck += left[:] + right[:]
        deck = shuffled_deck[:]  # Assigned back to deck in case there is another round of shuffling
    return deck


def split_deck(deck=[]):
    """
    Function that split the deck in a random number of cards
    :param deck: List of cards (String) to split
    :return: two List of cards
    """
    if deck and len(deck) > 1:
        index = randint(1, len(deck))
        left = deck[: index]
        right = deck[index:]
    else:
        left = deck
        right = []
    return left, right


def deal_cards(deck=[]):
    """
    Function that pick 5 cards per player from the top of the dec
    :param deck: List of cards (String) entire deck
    :return: 5 list of cards (String), first 4 list are cars for player , the last list is the leftover of the deck
    """

    player_1 = []
    player_2 = []
    player_3 = []
    player_4 = []
    for _ in range(4):
        for _ in range(5):
            print(deck.pop())



    if len(deck) > (5 * 4):
        player_1 = deck[: 5]
        deck = deck[5:]
        player_2 = deck[: 5]
        deck = deck[5:]
        player_3 = deck[: 5]
        deck = deck[5:]
        player_4 = deck[: 5]

    return player_1, player_2, player_3, player_4, deck