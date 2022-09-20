"""
	Description: Removes a char from a text (both inputed by the user)
	Author: Millan
	Date: 9/20/22
"""

from __future__ import annotations  # type hint support


def clean_string(text: str, char: str) -> str:
    """
    Purpose: Removes all instances of char from text
    Parameters: the base text to use (str), the char to remove from the string (str, len=1)
    Return Val: the text with all instances of char removed (str)
    """
    if len(text) == 0:
        return ""
    if text[0] == char:
        return clean_string(text[1:], char)
    return text[0] + clean_string(text[1:], char)


def get_char() -> str:
    """
    Purpose: gets a string with a length of one from the user
    Parameters: None
    Return Val: a string with a length of one (str)
    """
    while True:
        try:
            char = input("ch    : ")
            assert len(char) == 1
            return char
        except:
            print("Invalid. Please enter a single character.")


def main():
    text = input("string: ")
    char = get_char()

    cleaned_string = clean_string(text, char)
    print(cleaned_string)


main()
