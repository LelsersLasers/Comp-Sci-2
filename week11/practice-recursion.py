from __future__ import annotations  # type hint support
from typing import Any  # support for explicit 'Any' type


def fibonacci(N: int) -> int:
    if N <= 1:
        return N
    return fibonacci(N - 1) + fibonacci(N - 2)


def fibonacci_head_tail(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci_head_tail(n - 1, b, a + b)


def is_sorted(L: list[Any]) -> bool:
    if len(L) <= 1:
        return True
    elif L[0] > L[1]:
        return False
    return is_sorted(L[1:])


def main():
    print([fibonacci(n) for n in range(20)])
    print([fibonacci_head_tail(n) for n in range(20)])

    L1 = list(range(0, 20))
    L2 = list(range(20, 0, -1))
    print(is_sorted(L1))
    print(is_sorted(L2))


main()
