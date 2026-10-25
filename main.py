from games import roulette, profiles, fruitmachine, blackjack


def show_balance():
    print(f"""
    Saldo informatie
    ---------------------------
    Huidig saldo:   €{profiles.get_current_balance():.2f}
    ---------------------------
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

def show_account_menu():
    print("""
    --------------
    1.Laat alle accounts zien
    2.Maak nieuw account
    3.Wissel account
    4.Verwijder account
    0.Terug
    """)



def main():
    profiles.initialise_player()
    while True:
        salutation = profiles.determine_salutation(profiles.players[profiles.current_player]['name'], profiles.players[profiles.current_player]['gender'])
        if profiles.get_current_balance() < 1 :
            print(f"""{salutation}, Bedankt voor uw bezoek!
                    Eindsaldo: {profiles.get_current_balance():.2f}""")
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
                profiles.update_balance(fruitmachine.play(profiles.get_current_balance()))
                profiles.register_games_played("fruitmachine")
            elif choice == 2:
                profiles.update_balance(roulette.play(profiles.get_current_balance()))
                profiles.register_games_played("roulette")
            elif choice == 3:
                profiles.update_balance(blackjack.play_blackjack(profiles.get_current_balance()))
                profiles.register_games_played("blackjack")
            elif choice == 0:
                pass
            else:
                print("Voer een geldige keuze in!")
                continue

        elif choice == 2:
            show_balance()
        elif choice == 3:
            profiles.show_account()
            show_account_menu()
            account_menu_choice = int(input("Maak uw keuze: "))
            if account_menu_choice < 0 or account_menu_choice > 4:
                print("Kies een nummer van 0 tm 4!")
            elif account_menu_choice == 1:
                profiles.show_all_players()
            elif account_menu_choice == 2:
                profiles.create_user()
            elif account_menu_choice == 3:
                profiles.switch_account()
            elif account_menu_choice == 4:
                profiles.remove_account()
            elif account_menu_choice == 0:
                pass



        elif choice == 0:
            print(f"""{salutation} bedankt voor uw bezoek!
Eindsaldo: {profiles.get_current_balance():.2f}""")
            exit(0)

profiles.create_start_accounts()
# welkomstbanner
print("-" * 100)
print(" " * 32 + "WELKOM BIJ CASINO DE GOUDEN DRAAK")
print("-" * 100)
main()


