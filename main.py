
print("-" *100)
print(" "* 32+ "WELKOM BIJ CASINO DE GOUDEN DRAAK")
print("-" *100)

playerName = input("Voer uw naam in: ").title()
playerGender = input("Voer uw geslacht in (Man/Vrouw/Anders): ").title()
playerBirthday = input("Voer uw geboortedatum in (dd-mm-yyyy): ")
startingBudget = float(input("Voer uw budget in:€ "))

playerTitle = ""
if playerGender == "Man":
    playerTitle = f"Meneer {playerName}"
elif playerGender == "Vrouw":
    playerTitle = f"Mevrouw {playerName}"
else:
    playerTitle = f"Gast {playerName}"


TOEGANGSTICKET = 18.50
CONSUMPTIE = 6.50
GOKBELASTING = 3.33

VASTEKOSTEN = TOEGANGSTICKET + CONSUMPTIE + GOKBELASTING

gokBudget = startingBudget - VASTEKOSTEN

toegang = False
if  gokBudget >= 25:
    toegang = True

if toegang == True:
    print(f"""
Casino de Gouden Draak
--------------------------------
Startbudget:    €{startingBudget:.2f}
Vaste Kosten:   €{VASTEKOSTEN:.2f}
Gokbudget:      €{gokBudget:.2f}

{playerTitle} u heeft genoeg budget om te gokken, welkom in ons casino!""")

print("-" *100)
print(" "* 32+ "WELKOM BIJ CASINO DE GOUDEN DRAAK")
print("-" *100)