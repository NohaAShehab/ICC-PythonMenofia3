from crudDemo import register, login


def mainMenu():
    choice = input("Please enter l for login , r for register ")
    if choice == "r":
        register()
    elif choice == "l":
        login()


mainMenu()
