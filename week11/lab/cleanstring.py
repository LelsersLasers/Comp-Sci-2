from __future__ import annotations  # type hint support
# from typing import Any  # support for explicit 'Any' type


def clean_string(text: str, char: str) -> str:
    if len(text) == 0:
        return ""
    if text[0] == char:
        return clean_string(text[1:], char)
    return text[0] + clean_string(text[1:], char)

def get_char() -> str:
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