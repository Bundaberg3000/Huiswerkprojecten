from games import stake


def determine_rolls(round_number):
    if round_number % 5 == 1 :
        return "kers", "citroen", "ster"
    elif round_number % 5 == 2 :
        return "kers", "kers", "kers"
    elif round_number % 5 == 3 :
        return "ster", "ster", "citroen"
    elif round_number % 5 == 4 :
        return "citroen", "kers", "ster"
    return "ster", "ster", "ster"

def determine_payout(roll1, roll2, roll3, inzet):
    if roll1 == roll2 and roll1 == roll3:
        payout = inzet * 3
    elif roll1 == roll2 or roll1 == roll3 or roll2 == roll3:
        payout = inzet * 1
    else:
        payout = 0
    return payout


def play(balance):
    print("Welkom bij de fruitmachine")
    print("--------------------------")
    print(f"Uw saldo is {balance:.2f}")
    print(" ")
    round_number = 1
    while True:
        print("""
        1. Spelen
        0. Stop""")
        choice = int(input("Kies 0 of 1 :"))
        if not choice == 0 and not choice == 1:
            print("Voer een geldige keuze in!")
            continue
        elif choice == 0:
            return balance

        inzet = stake.stake(balance)
        balance -= inzet

        roll1, roll2, roll3, = determine_rolls(round_number)
        print(" ")
        print(roll1, roll2, roll3)
        print(" ")

        payout = determine_payout(roll1, roll2, roll3, inzet)
        if payout > 0:
            balance += payout
            print(f"Je hebt {payout:.2f} gewonnen!")
        else:
            print("Je hebt verloren...")
        print(f"Je nieuwe saldo is: {balance:.2f}")
        if balance < 1:
            print("Uw geld is op! Doei!")
            return balance

        round_number += 1
    return balance







