def stake(balance):
    while True:
        inzet =float((input("Hoeveel wilt u inzetten? :")))
        if inzet <= 0:
            print("Inzet mag geen 0 of minder dan 0 zijn!")
            continue
        elif inzet > balance:
            print("U kan niet meer inzetten dan u heeft!")
            continue
        else:
            return inzet