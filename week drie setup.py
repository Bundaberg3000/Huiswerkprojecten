#declareren constanten
TOEGANGSTICKET = 18.50
CONSUMPTIE = 6.50
GOKBELASTING = 3.33
VASTE_KOSTEN = TOEGANGSTICKET + CONSUMPTIE + GOKBELASTING
MIN_BUDGET = 25
MIN_AGE = 18
CURRENT_YEAR = 2026



def calculate_age(birthdate):
    birth_day, birth_month, birth_year = birthdate.split("-")
    age = CURRENT_YEAR - int(birth_year)
    return age

def check_age(birthdate):
    age = calculate_age(birthdate)
    if age < MIN_AGE:
        print(f"u bent nog geen {MIN_AGE}! Toegang is vanaf 18 jaar, tot ziens.")
    else:
        return birthdate

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
        print(f"{salutation}, u genoeg budget om te gokken, welkom in ons casino!")
    else:
        print(f"{salutation}, u heeft helaas niet genoeg budget om te gokken, tot ziens!")
        exit(1)



