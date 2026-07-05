import random

class Card:
    """Represents a playing card with a suit and rank."""

    def __init__(self, suit: str, rank: str):
        self.suit = suit  # e.g. "Hearts"
        self.rank = rank  # e.g. "K", "10", "A"

    def value(self) -> int:
        """
        Returns the numeric value of the card.
        TODO: Map ranks to values. 2-10 = 2-10, J = 11, Q = 12, K = 13, A = 14
        """
        card_values = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }
        return card_values[self.rank]

    def __str__(self) -> str:
        """Returns string representation like 'A of Spades'."""
        return f"{self.rank} of {self.suit}"


class Deck:
    """Represents a standard 52-card deck."""

    def __init__(self):
        self.cards: list = []  # list of Card objects
        self._create_deck()

    def _create_deck(self) -> None:
        """
        Populates the deck with 52 cards.
        TODO: Create cards for all combinations of 4 suits and 13 ranks.
        """
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))


    def shuffle(self) -> None:
        """Randomly shuffles the deck."""
        # TODO: Shuffle self.cards bonus
        random.shuffle(self.cards)

    def split(self) -> tuple:
        """
        Splits the deck into two halves.
        Returns:
            (list, list): Two lists of Card objects
        """
        first_half = self.cards[:int(len(self.cards) / 2)]
        second_half = self.cards[int(len(self.cards) / 2):]
        return first_half, second_half

def play_round(card1: Card, card2: Card) -> int:
    """
    Compares two cards and determines the winner.
    Returns:
        1 if card1 wins
        2 if card2 wins
        0 if tie
    TODO: Compare using value()
    """
    if card1.value() > card2.value():
        return 1
    elif card1.value() < card2.value():
        return 2
    else:
        return 0

def play_game(deck1: list, deck2: list) -> None:
    """
    Main game loop. Runs 26 rounds and tracks score.
    TODO: Loop over both decks, compare cards, update scores, and print result.
    """
    player1 = 0
    player2 = 0

    for card1, card2 in zip(deck1, deck2):
        result = play_round(card1, card2)
        if result == 1:
            player1 += 1
        if result == 2:
            player2 += 1

    if player1 > player2:
        print("Player1 wins")
    elif player2 > player1:
        print("Player2 wins")
    else:
        print("draw")

def main() -> None:
    """
    Game entry point.
    TODO:
    - Create deck
    - Shuffle
    - Split into two decks
    - Run play_game
    """
    deck = Deck()
    deck.shuffle()
    deck = deck.split()

    deck1 = deck[0]
    deck2 = deck[1]

    play_game(deck1, deck2)

if __name__ == "__main__":
    main()
