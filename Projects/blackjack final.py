import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return ''.join((self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["♠", "♥", "♦", "♣"]
                      for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]

    def shuffle_card(self):
        random.shuffle(self.cards)

    def random_card(self):
        return self.cards.pop(0)

class Player:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.point = 0

    def get_card(self, card):
        self.cards.append(card)

    def calculate_point(self):
        self.point = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.point += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.point += 11
                else:
                    self.point += 10
        if has_ace and self.point > 21:
            self.point -= 10
        return self.point

    def show_card_and_point(self):
        if self.dealer:
            print(self.cards[1], end=' '), print('<hidden>')
        else:
            for card in self.cards:
                print(card, end=' ')

            print("\nPlayer's point:"), print(self.calculate_point())

def play():
    playing = True

    while playing:
        deck = Deck()
        deck.shuffle_card()

        player_hand = Player()
        dealer_hand = Player(dealer=True)

        for i in range(2):
            player_hand.get_card(deck.random_card())
            dealer_hand.get_card(deck.random_card())

        print()
        print("Player:")
        player_hand.show_card_and_point()
        print()
        print("Dealer:")
        dealer_hand.show_card_and_point()

        game_over = False

        while not game_over:
            player_hand_value = player_hand.calculate_point()
            dealer_hand_value = dealer_hand.calculate_point()

            choice = input('Hit or stand? ').title()
            while choice not in ["H", "S", "Hit", "Stand"]:
                choice = input("Please enter 'Hit' or 'Stand' (H, S)").title()

            if choice in ['Hit', 'H']:
                player_hand.get_card(deck.random_card())
                print('Player:'), player_hand.show_card_and_point()
                if player_hand.calculate_point() > 21:
                    print("\nYou're busted :(")
                    game_over = True
            else:
                print()
                print("---------------- Result -----------------\n")
                print("Player:\n", player_hand_value)
                print("Dealer:\n", dealer_hand_value)

                if player_hand_value == 21:
                    print('You got blackjack! :D')

                elif player_hand_value > dealer_hand_value:
                    print()
                    print("You Win!")

                elif player_hand_value == dealer_hand_value:
                    print()
                    print("It's a push (Tie) :O")

                elif dealer_hand_value == 21:
                    print()
                    print('Dealer got blackjack :O')

                else:
                    print()
                    print("Dealer wins :O")
                game_over = True

        again = input("\nPlay Again? [Y/N] ")
        while again.title() not in ["Y", "N"]:
            again = input("Please enter Y or N ")
        if again.title() == "N":
            print()
            print("Thanks for playing! :D")
            playing = False
        else:
            game_over = False

print('---------- Welcome to Blackjack ----------')

if __name__ == "__main__":
    play()