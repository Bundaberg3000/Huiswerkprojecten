#welkomstboodschap
print("-" * 100)
print(" " * 32 + "WELKOM BIJ CASINO DE GOUDEN DRAAK")
print("-" * 100)

#declareren constanten
TOEGANGSTICKET = 18.50
CONSUMPTIE = 6.50
GOKBELASTING = 3.33
VASTE_KOSTEN = TOEGANGSTICKET + CONSUMPTIE + GOKBELASTING
MIN_BUDGET = 25
MIN_AGE = 18

#input vragen aan de speler
player_name = input("Voer uw naam in : ").title()
player_gender = input("Voer uw geslacht in (Man/Vrouw/Anders): ").title()
player_birthday = input("Voer uw geboortedatum in (dd-mm-yyyy): ")

#Bepalen leeftijd en checken of speler 18+ is
birth_day, birth_month, birth_year = player_birthday.split("-")

age = 2026 - int(birth_year)
if age < MIN_AGE:
    print(f"Je bent nog geen {MIN_AGE}! Toegang is vanaf 18 jaar, tot ziens.")
    exit(1)

starting_budget = float(input("Voer uw budget in:€ "))

#Aanspreek vorm bepalen
if player_gender == "Man":
    player_title = f"Meneer {player_name}"
elif player_gender == "Vrouw":
    player_title = f"Mevrouw {player_name}"
else:
    player_title = f"Gast {player_name}"

#Budget speler vragen ,checken en weergeven
starting_budget = float(input("Voer uw budget in:€ "))
balance = starting_budget - VASTE_KOSTEN

print(f"""
Casino de Gouden Draak
--------------------------------
Startbudget:    €{starting_budget:.2f}
Toegangsticket: €{TOEGANGSTICKET:.2f}
Consumptie:     €{CONSUMPTIE:.2f}
Gokbelasting:   €{GOKBELASTING:.2f}
Saldo:          €{balance:.2f}

""")
#Bepalen of de spelere genoeg budget heeft om te gokken
if  balance >= MIN_BUDGET:
    print(f"{player_title}, u heeft genoeg budget om te gokken, welkom in ons casino!")
else:
    print(f"{player_title}, u heeft helaas niet genoeg budget om te gokken, tot ziens!")
    exit(1)

#Het casino spel
round_number = 1

while True:
    print("""
    1:  Rood
    2:  Zwart
    3:  Even
    4:  Oneven
    0:  Stop""")
    choice = int(input("Kies je gok (0 om te stoppen) :"))
    if choice < 0 or choice > 4:
        print("Voer een geldige keuze in!")
        continue
    if choice == 0:
        break
    stake = float(input("Hoeveel wil je inzetten? :"))
    if stake <= 0:
        print("Inzet mag geen 0 of minder dan 0 zijn!")
        continue
    if stake > balance:
        print("Je kan niet meer inzetten dan je hebt!")
        continue
    balance -= stake
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
    win = False
    if choice == 1 and color == "Rood":
        win = True
    elif choice == 2 and color == "Zwart":
        win = True
    elif choice == 3 and odd_even == "Even":
        win = True
    elif choice == 4 and odd_even == "Oneven":
        win = True
    print(f"De bal valt op {color} {spin}.")
    if win:
        balance += stake * 2
        print(f"Je hebt gewonnen! Je wint {stake:.2f}!")
        print(f"Nieuw saldo: {balance:.2f}")
    else:
        print("Je verliest je inzet!")
        print(f"Nieuw saldo: {balance:.2f}")
    #Bepalen of de speler zijn geld op is en stoppen van het spel
    if balance  < 1:
        print("Je geld is op, DOEI!")
        break
    round_number += 1


#exit boodschap
print(f"Eindsaldo: {balance:.2f}")
print(f"{player_title} bedankt voor het spelen en tot ziens!")
