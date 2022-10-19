from __future__ import annotations  # type hint support
from swindle import *


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


def write_user_settings(filename: str, user_swindle: Swindle) -> None:
    settings = []
    settings.append(user_swindle.owner)
    for book in user_swindle.owned_books:
        settings.append(str(book) + ",owned")
    for book in user_swindle.available_books:
        settings.append(str(book) + ",available")
    with open(filename, "w", encoding="utf-8") as infile:
        for setting in settings:
            infile.write(setting + "\n")


def main():
    filename = "bookdb-large.txt"
    user_swindle = Swindle(filename)

    while True:
        menu_choice = main_menu()  # Display ereader's main menu
        if menu_choice == 1:
            user_swindle.buy()  # View available books with option to buy
        elif menu_choice == 2:
            user_swindle.show_owned()  # View owned books
        elif menu_choice == 3:
            user_swindle.read()  # Choose a book to read
        else:
            write_user_settings(filename, user_swindle)
            break  # Turn off ereader (quit the program)


main()
