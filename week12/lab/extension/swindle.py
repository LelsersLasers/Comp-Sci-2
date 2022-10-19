"""
Description: Is the class file for the swindle class. It also reads the database
			 of the books for their information, and not text
Author: Jerry and Millan
Date: 10/7/2022
"""

from __future__ import annotations  # type hint support
from book import *


def newUser() -> str:
    print("\nSince this is the first time you used it,")
    print("let's customize your Swindle...")
    owner = input("\nPlease enter your name: ")
    print("\nWelcome to %s's Swindle v1.0!" % owner)
    return owner


def read_book_database(filename: str) -> tuple[list[Book], list[Book], str]:
    """
    Purpose: read in book info from bookdb.txt, save each line as a Book object
                     in list. This list will be returned and will serve as available_books.
    Parameters: filename (str) that is the file with the text of the book
    Return Val: a list of the available books, a list of the owned books, and the owner's name
    """
    available_books: list[Book] = []
    owned_books: list[Book] = []
    with open(filename, "r", encoding="utf-8") as infile:
        num = 0
        for line in infile:
            line = line.strip()
            if line == "new_user":
                owner = newUser()
                num += 1
            elif num == 0:
                owner = line
                num += 1
            else:
                items = line.split(",")
                # items = [title, author, year, filename, ?available?, ?bookmark?]
                book = Book(items[0], items[1], int(items[2]), items[3])
                available = True
                try:
                    available = items[5] != "owned"
                except:
                    pass
                if available:
                    available_books.append(book)
                else:
                    book.set_bookmark(int(items[4]))
                    owned_books.append(book)
    return available_books, owned_books, owner


class Swindle(object):
    """class for a single Swindle object"""

    def __init__(self, filename: str):
        """constructor for swindle object, given ________________________"""
        self.available_books, self.owned_books, self.owner = read_book_database(filename)
        self.page_length: int = 20

    def __str__(self):
        """pretty-print info about this object"""
        s = ""
        s += "owner: %s\n" % self.owner
        s += "page_length: %i\n" % self.page_length
        s += "owned books:\n"
        for book in self.owned_books:
            s += "Book: %s\n" % book.to_string()
        s += "available books:\n"
        for available_book in self.available_books:
            s += "Book: %s\n" % available_book.to_string()
        return s

    def get_letter(self):
        """This method determines what the user wants to do next"""
        valid_choices = ["n", "p", "q"]
        while True:
            reading_choice = str(input("\nn (next); p (previous); q (quit): "))
            if reading_choice in valid_choices:
                return reading_choice
            print("invalid input, try again")

    def display_page(self, book):
        """This method displays a single page at a time (300 chars)"""
        book_contents = book.get_text()
        book_lines_list = book_contents.split("\n")
        num_lines = len(book_lines_list)
        num_pages = num_lines // self.page_length  # calculate total number of pages in book
        page = book.get_bookmark()  # get current page (most recently read)
        page_start = page * self.page_length
        page_end = page_start + self.page_length  # display 20 lines per page
        if page_end > num_lines:
            page_end = num_lines  # in case you're at the end of the book
        for i in range(page_start, page_end):
            print(book_lines_list[i])
        if num_pages == 1:  # alter page numbers for 1-page books
            page = 1
        print("\nShowing page %d out of %d" % (page, num_pages))
        return

    def display_text(self, book):
        """This method allows the user to read one of their books.
        It calls display_page() to show a single page at a time.
        It calls get_letter() to determine what the user wants to do next.
        When the user decides to quit reading a particular book, this method
        returns the (updated) Book object.
        """
        while True:
            self.display_page(book)
            current_page = book.get_bookmark()
            choice = self.get_letter()  # user chooses to quit or read the next/previous page
            if choice == "q":  # quit reading and return to ereader
                return book
            elif choice == "n":  # move on to the next page in the book
                book_contents = book.get_text()  # unless user is on the last page
                num_lines = book_contents.count("\n")
                currentLine = current_page * self.page_length
                if (currentLine + 1) < (num_lines - self.page_length):
                    book.set_bookmark(current_page + 1)
                else:
                    print("\nThere are no more pages. Enter 'p' to go to the previous page or 'q' to quit.")
            else:  # return to previous page in the book
                book.set_bookmark(current_page - 1)

    def show_owned(self) -> None:
        """This method prints out the list of owned books"""
        num_owned = len(self.owned_books)
        if num_owned == 0:
            print("\nYou don't own any books.")
        else:
            print("\nBooks you own:")
            for idx in range(num_owned):
                print(" %i: %s" % (idx + 1, self.owned_books[idx].to_string()))
        return

    def show_available(self) -> None:
        """This method prints out the list of available books"""
        num_available = len(self.available_books)
        if num_available == 0:
            print("\nThere are no books available to purchase.")
        else:
            print("\nAvailable books:")
            for idx in range(num_available):
                print(" %i: %s" % (idx + 1, self.available_books[idx].to_string()))
        return

    def get_owner(self) -> str:
        return self.owner

    def buy(self) -> None:
        """This method allows the user to buy a book from the list of available books."""
        self.show_available()
        len_books = len(self.available_books)
        if len_books > 0:
            # minus 1 because index starts at 0
            index = get_valid_int("\nWhich book would you like to buy? (0 to skip): ", len_books) - 1
            if index >= 0:
                book = self.available_books.pop(index)
                self.owned_books.append(book)
                print("\nYou've successfully purchased the book: %s" % book.get_title())
        return

    def read(self) -> None:
        """This method allows the user to read one of their books."""
        self.show_owned()
        len_books = len(self.owned_books)
        if len_books > 0:
            # minus 1 because index starts at 0
            index = get_valid_int("\nWhich book would you like to read? (0 to skip): ", len_books) - 1
            if index >= 0:
                book = self.owned_books[index]
                self.display_text(book)
                print("\nSetting bookmark in %s at page %i" % (book.get_title(), book.get_bookmark()))
        return


def get_valid_int(prompt: str, max_value: int) -> int:
    """
    Purpose: Gets an integer from the user and is less than the maximum value
    Parameters: prompt (str) that is displayed to user and max_value (int) is the
                            value that the input should be less than
    Return Val: the integer that user inputs that has been checked is an integer
    """
    while True:
        user_input = input(prompt)
        try:
            user_int = int(user_input)
            assert user_int <= max_value
            return user_int
        except:
            print("invalid input, try again")


if __name__ == "__main__":
    print("Testing the Swindle class...")
    owner = "Lionel"
    my_swindle = Swindle(owner)

    print("Testing showAvailable...")
    my_swindle.show_available()

    print("Testing showOwned...")
    my_swindle.show_owned()

    ################ Write additional tests below ###################

    my_swindle.show_available()
    my_swindle.show_owned()
    print(my_swindle.get_owner())
    my_swindle.buy()
    my_swindle.read()
