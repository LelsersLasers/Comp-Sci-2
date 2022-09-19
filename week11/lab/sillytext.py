from __future__ import annotations  # type hint support
# from typing import Any  # support for explicit 'Any' type


def print_silly_text(text: str, num: int) -> None:
    if len(text) == 0:
        return
    print(text[0] * num, end="")
    print_silly_text(text[1:], num)


def get_pos_int() -> int:
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

    print("")
    print_silly_text(text, num)



main()