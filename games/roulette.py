from games import stake

#Het casino spel

def show_options():
    print("""
            1:  Rood
            2:  Zwart
            3:  Even
            4:  Oneven
            0:  Stop""")
    choice = int(input("Kies uw gok (0 om te stoppen) :"))
    return choice

def win_or_lose(choice, color, odd_even):
    if choice == 1 and color == "Rood":
        win = True
    elif choice == 2 and color == "Zwart":
        win = True
    elif choice == 3 and odd_even == "Even":
        win = True
    elif choice == 4 and odd_even == "Oneven":
        win = True
    else:
        win = False
    return win


def play(balance):
    round_number = 1
    while True:
        choice = show_options()
        if choice < 0 or choice > 4:
            print("Voer een geldige keuze (0 tm 4) in!")
            continue
        elif choice == 0:
            return balance
        inzet = stake.stake(balance)
        balance -= inzet

        spin = (round_number * 7) % 37

        if spin == 0:
            color = "Groen"
            odd_even = None
        elif spin <= 18:
            if spin % 2 == 0:
                color = "Zwart"
                odd_even = "Even"
            else:
                color = "Rood"
                odd_even = "Oneven"
        else:
            if spin % 2 == 0:
                color = "Rood"
                odd_even = "Even"
            else:
                color = "Zwart"
                odd_even = "Oneven"

        #bepalen of de speler gewonnen heeft en nieuw saldo bepalen
        win = win_or_lose(choice, color, odd_even)

        print(f"De bal valt op {color} {spin}.")
        if win:
            balance += inzet * 2
            print(f"U hebt gewonnen! U wint {inzet:.2f}!")
            print(f"Nieuw saldo: {balance:.2f}")

        else:
            print("U verliest uw inzet!")
            print(f"Nieuw saldo: {balance:.2f}")
        #Bepalen of de speler zijn geld op is en stoppen van het spel
        if balance  < 1:
            print("Uw geld is op, DOEI!")
            break
        round_number += 1


    #exit boodschap
    print(f"Eindsaldo: {balance:.2f}")
    return balance

