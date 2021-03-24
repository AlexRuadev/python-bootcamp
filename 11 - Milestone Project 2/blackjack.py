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


# print(test_deck)


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
# print(pulled_card)
# Add that card to the test_player hand
test_player.add_card(pulled_card)
# print(test_player.value)

# add a card to our deck
test_player.add_card(test_deck.deal())


# print(test_player.value)


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


# Create funcction for taking bets using try/except
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! You have can't bet more than", chips.total)
            else:
                break


# Create a function for taking hits.
def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


#  Writing a function asking the player to Hit or Stand
def hit_or_stand(deck, hand):

    # Controling an upcoming while loop
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player Stands, Dealer's turn")
            playing = False
        else:
            print("Sorry, I didn't understand that, Please enter h or s only")
            continue
        break


# Write function to display cards
def show_some(player, dealer):
    print("Dealer's Hand:")
    print("one card hidden")
    print(dealer.cards[1])
    print('\n')
    print("Player's Hand:")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print("Dealer's Hand:")
    for card in dealer.cards:
        print(card)
    print('\n')
    print("Player's Hand:")
    for card in player.cards:
        print(card)


# Write functions to handle the end of the game scenarios
def player_busts(player, dealer, chips):
    print('BUST PLAYER !')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('PLAYER WINS !')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('PLAYER WINS ! DEALER BUSTED !')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('DEALER WINS !')
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and Player tie! PUSH')


# Playing the game
while True:
    # Print an opening statement
    print('Welcome to BLACKJACK')

    # Create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

        # If Player hasn't busted, play Dealer's h and until Dealer reaches 17
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

                # show all cards
                show_all(player_hand, dealer_hand)

                # run different winning scenarios
                if dealer_hand.value > 21:
                    dealer_busts(player_hand, dealer_hand, player_chips)
                elif dealer_hand.value > player_hand.value:
                    dealer_wins(player_hand, dealer_hand, player_chips)
                elif dealer_hand.value < player_hand.value:
                    player_wins(player_hand, dealer_hand, player_chips)
                else:
                    push(player_hand, dealer_hand)

                # inform Player of remaining chips
                print('\n Player total chips are at: {}'.format(player_chips.total))
                # Ask to play again
                new_game = input("Would you like to play another hand? y/n")

                if new_game[0].lower() == 'y':
                    playing = True
                    continue
                else:
                    print('Thank you for playing')
                    break
