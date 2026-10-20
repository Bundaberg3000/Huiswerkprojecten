from games import roulette
from games import fruitmachine
from games import blackjack

#declareren constanten
TOEGANGSTICKET = 18.50
CONSUMPTIE = 6.50
GOKBELASTING = 3.33
VASTE_KOSTEN = TOEGANGSTICKET + CONSUMPTIE + GOKBELASTING
MIN_BUDGET = 25
MIN_AGE = 18
CURRENT_YEAR = 2026

def calculate_age(birthday):
    birth_day, birth_month, birth_year = birthday.split("-")
    age = CURRENT_YEAR - int(birth_year)
    return age

def check_age():
    while True:
        birthday = input("Voer je geboortedatum in (dd-mm-jjjj): ")
        if not birthday.count("-") == 2:
            print("Voer een geldige datum in aub.")
            continue
        age = calculate_age(birthday)
        if age < MIN_AGE:
            print(f"u bent nog geen {MIN_AGE}! Toegang is vanaf {MIN_AGE} jaar, tot ziens.")
            exit(1)
        else:
            return birthday


def determine_salutation(player_name,player_gender):
    if player_gender == "Man":
        salutation  = f"Meneer {player_name}"
    elif player_gender == "Vrouw":
        salutation = f"Mevrouw {player_name}"
    else:
        salutation = f"Gast {player_name}"

    return salutation

def show_welcome_message(starting_budget, balance, salutation):
    print(f"""
    Casino de Gouden Draak
    --------------------------------
    Startbudget:    €{starting_budget:.2f}
    Toegangsticket: €{TOEGANGSTICKET:.2f}
    Consumptie:     €{CONSUMPTIE:.2f}
    Gokbelasting:   €{GOKBELASTING:.2f}
    --------------------------------
    Saldo:          €{balance:.2f}

    """)
    if balance >= MIN_BUDGET:
        print(f"{salutation}, u heeft genoeg budget om te gokken, welkom in ons casino!")
    else:
        print(f"{salutation}, u heeft helaas niet genoeg budget om te gokken, tot ziens!")
        exit(1)

def show_balance(balance):
    print(f"""
    Saldo informatie
    ---------------------------
    Huidig saldo:   €{balance:.2f}
    ---------------------------
    """)

def show_account(salutation, birthdate, age):
    print(f"""
    Account info
    -----------------------------------------
    Naam:           {salutation}
    Geboortedatum:  {birthdate}
    leeftijd:       {age}
    -----------------------------------------
    """)

def show_games_menu():
    print("""
    ---------------
    1.Fruitmachine
    2.Roulette
    3.Blackjack
    0.Terug
    ---------------
    """)

def show_main_menu():
    print("""
    ------------
    1.Spellen
    2.Saldo
    3.Account
    0.Stop
    ------------
    """)

def main():

    #input vragen aan de speler
    salutation = determine_salutation(input("Voer uw naam in : ").title(), input("Voer uw geslacht in (Man/Vrouw/Anders): ").title())
    birthdate = check_age()
    starting_budget = float(input("Voer uw budget in:€ "))

    balance = starting_budget - VASTE_KOSTEN
    age = calculate_age(str(birthdate))

    show_welcome_message(starting_budget, balance, salutation)
    while True:
        if balance < 1 :
            print(f"""Bedankt voor uw bezoek!
                    Eindsaldo: {balance}""")
            exit(0)
        show_main_menu()

        choice = int(input("Maak uw keuze: "))
        if choice < 0 or choice > 3:
            print("Kies een nummer van 0 tm 3!")
            continue
        elif choice == 1:
            show_games_menu()
            choice = int(input("Maak uw keuze: "))
            if choice < 0 or choice > 3:
                print("Kies een nummer van 0 tm 3!")
            elif choice == 1:
                balance = fruitmachine.play(balance)
            elif choice == 2:
                balance = roulette.play(balance)
            elif choice == 3:
                balance = blackjack.play_blackjack(balance)
            elif choice == 0:
                break
            else:
                print("Voer een geldige keuze in!")
                continue

        elif choice == 2:
            show_balance(balance)
        elif choice == 3:
            show_account(salutation, birthdate, age)
        elif choice == 0:
            print(f"""Bedankt voor uw bezoek!
        Eindsaldo: {balance:.2f}""")
            exit(0)



# welkomstbanner
print("-" * 100)
print(" " * 32 + "WELKOM BIJ CASINO DE GOUDEN DRAAK")
print("-" * 100)
main()


