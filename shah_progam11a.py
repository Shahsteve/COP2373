import random

class Deck():

    def __init__():
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        deck = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def deal_self(deck, size=5):
        
        hand = []
        for _ in range(size):
            hand.append(deck.pop())
        return hand

    def print_hand(hand):
        for card in hand:
            print(f"{card[0]} of {card[1]}")

    def draw_new_cards(hand, deck, indices):
        for index in indices:
            if 0 <= index < len(hand):
                hand[index] = deck.pop()

    if __name__ == "__main__":

        print("Welcome to the poker hand! Dealing you in now!")
        deck = __init__()
        hand = deal_self(deck)

        print("Your 5 card poker hand:")
        print_hand(hand)

        discard_index = input("Enter the index of cards to replace (0-4(0=1st card, etc..), separated by spaces): ")
        discard_index = [int(x) for x in discard_index.split() if x.isdigit()]

        draw_new_cards(hand, deck, discard_index)

        print("Your new 5 card poker hand:")
        print_hand(hand)
