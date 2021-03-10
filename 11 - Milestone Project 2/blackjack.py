# Import random module to shuffle the deck before dealing.  Declare variables to store suits, ranks and values. Declare a boolean to controle the while loop

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Height', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Height': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


# Create a Card class with two attributes : suit and rank. We may add an attribute for 'Value'
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


# Create a Deck class. Add method to shuffle our deck and to deal our cards
class Deck:

    def __init__(self):
        # start with an empty list
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        # grab the deck attribute and pop off a card item from that list
        single_card = self.deck.pop()
        return single_card


test_deck = Deck()
test_deck.shuffle()
print(test_deck)


# Create a Hand class
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        # Add an attribute to keep track of aces
        self.aces = 0

    def add_card(self, card):
        #  card passed in
        #  from Deck.deal() --> single Card(suit, rank)
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # if total value > 21 and i still have an ace
        # then change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


test_deck = Deck()
test_deck.shuffle()

#  Define Player
test_player = Hand()
# Deal 1 card from the deck Card(suit, rank)
pulled_card = test_deck.deal()
print(pulled_card)
# Add that card to the test_player hand
test_player.add_card(pulled_card)
print(test_player.value)

# add a card to our deck
test_player.add_card(test_deck.deal())
print(test_player.value)


# Create a Chips class
class Chips:
    def __init__(self, total=100):
        # We set it with a default value
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
