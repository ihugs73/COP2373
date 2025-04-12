import random


class Card:
    """Represents a single playing card."""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    """Represents a deck of 52 cards."""

    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        """Returns one card from the deck (or None if the deck is empty)."""
        if self.cards:
            return self.cards.pop()
        return None


def display_hand(hand, message="Your hand:"):
    """Prints the cards in hand, each with its position."""
    print(message)
    for index, card in enumerate(hand, start=1):
        print(f"{index}: {card}")
    print()


def play_poker():
    """Main function to play a simple Poker hand replacement game."""

    # Create and shuffle deck
    deck = Deck()
    deck.shuffle()

    # Deal initial hand of 5 cards
    hand = [deck.deal_card() for _ in range(5)]
    display_hand(hand, "Your initial hand:")

    # Prompt user for the card positions to replace
    user_input = input("Enter the positions of cards to replace, separated by commas (e.g., 1, 3, 5): ")

    # Split the user input into a list of integers (positions)
    positions = [pos.strip() for pos in user_input.split(",")]
    # Filter and convert valid positions to int (1 through 5)
    positions = [int(pos) for pos in positions if pos.isdigit() and 1 <= int(pos) <= 5]
    # Remove duplicates and sort positions
    positions = sorted(set(positions))

    # Replace the selected cards with new ones from the deck
    for pos in positions:
        # Adjust for 0-based index
        hand[pos - 1] = deck.deal_card()

    # Display the new hand after drawing replacements
    display_hand(hand, "Your new hand:")


if __name__ == "__main__":
    play_poker()
