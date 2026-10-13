def stake(inzet, balance):
    if float(inzet) <= 0:
        print("Inzet mag geen 0 of minder dan 0 zijn!")
    elif float(inzet) > balance:
        print("U kan niet meer inzetten dan u heeft!")
    else:
        balance -= float(inzet)
    return balance, inzet


def play(balance):

    round_number = 1
    while True:
        print("Welkom bij de fruitmachine")
        print("--------------------------")
        print(f"Uw saldo is {balance}")
        print(" ")
        print("""
        1. Spelen
        0. Stop""")
        choice = int(input("Kies 1 of 0:"))
        if not choice == 0 and not choice == 1:
            print("Voer een geldige keuze in!")
            continue
        elif choice == 0:
            return balance
        elif choice == 1:
            balance, inzet = stake(float(input("Hoeveel wilt u inzetten? :")), balance)












