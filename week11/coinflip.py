import random


def coin_flip(n: int) -> int:
    if n <= 0:
        return 0
    return coin_flip(n - 1) + random.choice([0, 1])


def main():
    n = int(input("Enter number of flips: "))
    print(coin_flip(n), "heads")


main()
