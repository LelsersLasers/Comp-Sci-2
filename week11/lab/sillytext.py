"""
	Description: Repeats all the characters in a text based on how many times the
        user wants
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


def get_pos_int(prompt: str, low: int = None, high: int = None) -> int:
    """
    Purpose: gets a positive integer from the user
    Parameters: prompt (str) is the prompt to display, low (optional int) is the
        inclusive lower bound, high (optional int) is the inclusive upper bound
    Return Val: a positive integer (int)
    """
    while True:
        user_input = input(prompt)
        try:
            num = int(user_input)
            if low != None:
                assert num >= low
            if high != None:
                assert num <= high
            return num
        except:
            print("That is not a positive number.")


def main():
    text = input("string: ")
    num = get_pos_int("num: ", 0)

    sillified_text = silly_text(text, num)
    print("\n" + sillified_text)


main()
