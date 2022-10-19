from __future__ import annotations  # type hint support
from swindle import *


def newUser():
    print("\nSince this is the first time you used it,")
    print("let's customize your Swindle...")
    owner = str(input("\nPlease enter your name: "))
    print("\nWelcome to %s's Swindle v1.0!" % owner)
    return owner


def main_menu():
    print("\n--------------------------------------------------\n")
    print("1) Buy/See available books\n2) See owned books\n3) Read a book\n4) Exit\n")
    while True:
        user_input = str(input("---> "))
        try:
            menu_choice = int(user_input)
            if 1 <= menu_choice <= 4:
                return menu_choice
            else:
                print("invalid number, try again")
        except ValueError:
            print("invalid input, try again")


def main():

    owner = newUser()  # Display instructions and get user's name
    user_swindle = Swindle(owner)  # Create a new Swindle ereader for them

    while True:
        menu_choice = main_menu()  # Display ereader's main menu
        if menu_choice == 1:
            user_swindle.buy()  # View available books with option to buy
        elif menu_choice == 2:
            user_swindle.show_owned()  # View owned books
        elif menu_choice == 3:
            user_swindle.read()  # Choose a book to read
        else:
            break  # Turn off ereader (quit the program)


main()
