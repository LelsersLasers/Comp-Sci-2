"""
	Description: Repeats all the characters in a text based on how many times the user wants
	Author: Millan
	Date: 9/20/22
"""

from __future__ import annotations  # type hint support


def multiply_str(string: str, num: int) -> str:
    """
    Purpose: does string * num
    Parameters: the char to print (str), the number of times remaining to print (int)
    Return Val: the string repeated num times (str)
    """
    if num == 0:
        return ""
    else:
        return string + multiply_str(string, num - 1)


def silly_text(text: str, num: int) -> str:
    """
    Purpose: returns text with each character repeated num times
    Parameters: the base text use (str), the number of times to repeat each character (int)
    Return Val: the text with each character repeated num times
    """
    if len(text) == 0:
        return ""
    else:
        return multiply_str(text[0], num) + silly_text(text[1:], num)


def get_pos_int() -> int:
    """
    Purpose: gets a positive integer from the user
    Parameters: None
    Return Val: a positive integer (int)
    """
    while True:
        try:
            num = int(input("num: "))
            assert num >= 0
            return num
        except:
            print("That is not a positive number.")


def main():
    text = input("string: ")
    num = get_pos_int()

    sillified_text = silly_text(text, num)
    print("\n" + sillified_text)


main()
