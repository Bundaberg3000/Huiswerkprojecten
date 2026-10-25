MIN_AGE = 18
CURRENT_YEAR = 2026
TOEGANGSTICKET = 18.50
CONSUMPTIE = 6.50
GOKBELASTING = 3.33
VASTE_KOSTEN = TOEGANGSTICKET + CONSUMPTIE + GOKBELASTING
MIN_BUDGET = 25

players = {}
current_player = None

def create_user(player_name=None):
    if player_name is None:
        player_name = check_for_name()
    birthday = check_age()

    if birthday is None:
        print(f"U bent nog te jong! Toegang is vanaf {MIN_AGE}.")
        return False

    player_gender = input("Voer uw geslacht in (Man/Vrouw/Anders): ").strip().title()
    balance = check_budget(float(input("Voer uw budget in:€ ")))
    if balance is None:
        print("U heeft niet genoeg budget!")
        return False

    create_user_profile(player_name, birthday, player_gender, balance)
    salutation = determine_salutation(player_name, player_gender)
    print(" ")
    print(f"Welkom {salutation} in ons casino! Gok Verstandig.")
    return True


def check_for_name():
    while True:
        name = input("Voer uw naam in :").strip().title()
        if name in players:
            print("Naam bestaat al, kies een andere naam..")
        else:
            return name


def initialise_player():
    global current_player
    global players
    player_name = input("Voer uw naam in :").title().strip()
    current_player = player_name
    if player_name in players:
        salutation = determine_salutation(current_player, players[current_player]['gender'])
        print(f"Welkom terug {salutation}!")
        print(f"Huidig saldo: {players[current_player]['saldo']:.2f}")
    else:
        check_acces = create_user(player_name)
        if check_acces is False:
            exit(0)




def create_user_profile(player_name, birthday, player_gender, balance):
    players[player_name] = {'name':player_name.title(), 'birthday': birthday, 'gender':player_gender.title(), 'saldo':balance, 'gespeelde_spellen':{}}


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
            return None
        else:
            return birthday


def determine_salutation(player_name, player_gender):
    if player_gender == "Man":
        salutation  = f"Meneer {player_name}"
    elif player_gender == "Vrouw":
        salutation = f"Mevrouw {player_name}"
    else:
        salutation = f"Gast {player_name}"

    return salutation


def check_budget(starting_budget):
    balance = starting_budget - VASTE_KOSTEN
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
        print("U heeft genoeg budget om te mogen gokken!")
        return balance
    else:
        return None

def create_start_accounts():
    create_user_profile('Erik', '20-02-2000', 'anders', 900)
    create_user_profile('Simone', '21-03-2001', 'vrouw', 800)
    create_user_profile('Jeroen', '22-02-1999', 'man', 1000)
    create_user_profile('Femke', '19-01-1997', 'vrouw', 1500)

def show_account():
    current_account = players[current_player]
    print(f"Naam:               {current_account['name']}")
    print(f"Verjaardag:         {current_account['birthday']}")
    print(f"Gender:             {current_account['gender']}")
    print(f"Saldo:              {current_account['saldo']:.2f}")
    print(f"Gespeelde spellen:  {current_account['gespeelde_spellen']}")
    print(" ")
    print("Beschikbare spelers:")
    print(list(players.keys()))

def update_balance(balance):
    global players
    players[current_player].update({'saldo': balance})


def show_all_players():
    for player in players.values():
        print(f"{player.get('name')}: Saldo: {player.get('saldo'):.2f}")

def switch_account():
    global current_player
    select_account = input("Naar welke account wilt u wisselen?: ").strip().title()
    if select_account in players:
        current_player = select_account
    else:
        print("Account bestaat niet...")
        return

def remove_account():
    global players
    account_to_remove = input("Welke account wilt u verwijderen?: ").strip().title()
    if account_to_remove in players:
        if len(players) == 1:
            print("Laatste account in het systeem kan niet verwijderd worden!")
            return
        elif account_to_remove == current_player:
            print("Huidig spelende account kan niet worden verwijderd, wissel eerst van account!")
            return
        else:
            del players[account_to_remove]
            print(f"Account {account_to_remove} verwijderd")
    else:
        print("Naam niet gevonden!")


def get_current_balance():
    return players[current_player]['saldo']

def register_games_played(game_name):
    global players
    spellen = players[current_player]['gespeelde_spellen']
    if game_name in spellen:
        spellen[game_name] += 1
    else:
        spellen[game_name] = 1