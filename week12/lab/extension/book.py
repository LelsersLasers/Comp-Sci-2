"""
Description: Is a class file for a book object with functions
Author: Jerry and Millan
Date: 10/7/2022
"""

from __future__ import annotations  # type hint support


class Book(object):
    """class for a single Book object"""

    def __init__(self, title: str, author: str, year: int, filename: str):
        """constructor for book object, given ____________________"""
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.filename: str = filename
        self.bookmark: int = 0

    def __str__(self):
        """pretty-print info about this object"""
        return "%s,%s,%i,%s,%i" % (
            self.title,
            self.author,
            self.year,
            self.filename,
            self.bookmark,
        )

    def to_string(self) -> str:
        """Displays info about the book"""
        return "%25s by %20s (%i)" % (self.title, self.author, self.year)

    def get_title(self) -> str:
        return self.title

    def set_title(self, title: str) -> None:
        self.title = title

    def get_author(self) -> str:
        return self.author

    def set_author(self, author: str) -> None:
        self.author = author

    def get_year(self) -> int:
        return self.year

    def set_year(self, year: int) -> None:
        self.year = year

    def get_filename(self) -> str:
        return self.filename

    def set_filename(self, filename: str) -> None:
        self.filename = filename

    def get_bookmark(self) -> int:
        return self.bookmark

    def set_bookmark(self, bookmark) -> None:
        self.bookmark = bookmark

    def get_text(self) -> str:
        """gets the text from the book file"""
        text = ""
        with open(self.filename, "r", encoding="utf-8") as infile:
            for line in infile:
                if line[0] != "#":
                    text += line
        return text


if __name__ == "__main__":

    print("Testing the Book class...")
    my_book = Book("Gettysburg Address", "Abe Lincoln", 1863, "book-database/gettysburg.txt")
    print(my_book)

    print("Testing toString...")
    print(my_book.to_string())

    print("Testing getFilename...")
    print(my_book.get_filename())

    print("Testing getText...")
    text = my_book.get_text()
    print(text[:105])  # only print the first couple of lines

    print("bookmark is:", my_book.get_bookmark())
    my_book.set_bookmark(12)
    print("now bookmark is:", my_book.get_bookmark())

    ################ Write additional tests below ###################

    print("the author is:", my_book.get_author())
    my_book.set_author("Jerry Huber")
    print("author is now:", my_book.get_author())

    print("the year is:", my_book.get_year())
    my_book.set_year(2022)
    print("year is now:", my_book.get_year())

    print(my_book.to_string())
