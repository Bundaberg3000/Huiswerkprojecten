import random
from games import stake

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def create_deck():
    deck_list = [f"{suit}{rank}" for suit in SUITS for rank in RANKS]
    random.shuffle(deck_list)
    return deck_list

def draw_card(deck, hand):
    hand.append(deck.pop())

def show_hand(dealer_hand=None, player_hand=None,hide_card=False):
    if dealer_hand:
        if hide_card:
            print(f"Dealer hand: {dealer_hand[0]} | ??")
        else:
            print(f"Dealer hand: {' | '.join(dealer_hand)}")
    if player_hand:
        print(f"Player hand: {' | '.join(player_hand)}")

def calculate_card_value(card):
    rank = card[1:]
    if rank in ('J', 'Q', 'K'):
        return 10
    elif rank == 'A':
        return 11
    else:
        return int(rank)

def calculate_hand_value(hand):
    score = 0
    for card in hand:
        score += calculate_card_value(card)
    return score

def count_aces(hand):
    number_of_aces = 0
    for card in hand:
        if card[1:] == 'A':
            number_of_aces += 1
    return number_of_aces

def total_score(hand):
    score = calculate_hand_value(hand)
    number_of_aces = count_aces(hand)
    while score > 21 and number_of_aces > 0:
        score -= 10
        number_of_aces -= 1
    return score


def play_blackjack(balance):
        while True:
            if balance < 1:
                print("Uw geld is op! Doei!")
                print(f"Eindsaldo: {balance:.2f}")
                exit(0)
            print("1. Spelen")
            print("0. Stop")
            choice = int(input("Kies 0 of 1 :"))
            if not choice == 0 and not choice == 1:
                print("Voer een geldige keuze in!")
                continue
            elif choice == 0:
                print(f"Uw saldo na blackjack: {balance:.2f}")
                return balance

            inzet = stake.stake(balance)
            balance -= inzet
            deck = create_deck()
            player_hand = []
            dealer_hand = []
            for i in range(2):
                draw_card(deck, player_hand)
            for i in range(2):
                draw_card(deck, dealer_hand)
            show_hand(dealer_hand, player_hand, True)
            player_score = total_score(player_hand)
            print(f"Uw score: {player_score}")
            while True:
                if player_score < 21:
                    choice = input("Hit or Stand? :").title().strip()
                    if choice == 'Hit':
                        draw_card(deck, player_hand)
                        print(f"U trekt {player_hand[-1]}")
                        show_hand(None,player_hand)
                        player_score = total_score(player_hand)
                        print(f"Uw score: {player_score}")
                    elif choice == 'Stand':
                        print(f"U stopt op {player_score}")
                        show_hand(None,player_hand)
                        break
                    else:
                        print("Voer een geldige keuze in!")
                        continue
                elif player_score == 21:
                    print(f"U heeft {player_score}!")
                    show_hand(None,player_hand)
                    break
                elif player_score > 21:
                    print("-------BUST---------")
                    print("U verliest uw inzet")
                    show_hand(None, player_hand)
                    break
            if not player_score > 21:
                print("-------------")
                print("Dealers beurt")
                print("-------------")
                show_hand(dealer_hand, None, False)
                dealer_score = total_score(dealer_hand)
                print(f"Dealer score: {dealer_score}")
                while True:
                    if dealer_score < 17:
                        draw_card(deck, dealer_hand)
                        print(f"Dealer trekt {dealer_hand[-1]}")
                        show_hand(dealer_hand, None, False)
                        dealer_score = total_score(dealer_hand)
                        print(f"Dealer score: {dealer_score}")
                    elif dealer_score >= 17 and dealer_score < 22:
                        print(f"Dealer stands at {dealer_score}")
                        show_hand(dealer_hand, None, False)
                        break
                    elif dealer_score > 21:
                        print("Dealer BUST")
                        show_hand(dealer_hand, None, False)
                        break
                print(f"Uw score :      {player_score}")
                print(f"Dealer score :  {dealer_score}")
                if dealer_score > 21:
                    balance += inzet * 2
                    print(f"U wint 2x uw inzet!")
                    print(f"New balance: {balance:.2f}")
                    break
                elif player_score > dealer_score:
                    balance += inzet * 1.5
                    print(f"U wint 1.5x uw inzet!")
                    print(f"New balance: {balance:.2f}")
                    break
                elif player_score == dealer_score:
                    balance += inzet
                    print(f"U wint uw inzet terug!")
                    print(f"New balance: {balance:.2f}")
                    break
                else:
                    print("Dealer wint! U verliest uw inzet...")
                    break

