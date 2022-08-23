"""
    Description: Collection of sorting algrothrims
    Author: Millan
    Date: 8/23/22
"""


from __future__ import annotations  # type hint support
from typing import Any  # support for explicit 'Any' type


def make_list(n: int) -> list[int]:
    """
    Purpose: Makes a list of integers 0 to n
    Parameters: n (int) the length of the list
    Return val: A list of integers 0 to n
    """
    return [i for i in range(n)]


def copy_list(arr: list[Any]) -> list[Any]:
    """
    Purpose: Copies a list
    Parameters: arr (list) the list to copy
    Return val: The copied list
    """
    return [x for x in arr]


def my_sort(arr: list[Any]) -> list[Any]:
    """
    Purpose: Sorts a list
    Parameters: arr (list) the list to be sorted
    Return val: A copy of the sorted list
    """
    new_arr = copy_list(arr)  # does not change orginal list
    for i in range(len(new_arr) - 1):
        lowest_idx = len(new_arr) - 1
        for j in range(i, len(new_arr) - 1):
            if new_arr[j] < new_arr[lowest_idx]:
                lowest_idx = j
        lowest = new_arr.pop(lowest_idx)
        new_arr.insert(i, lowest)
    return new_arr


if __name__ == "__main__":
    import random  # for random shuffle

    arr_len = 200

    starting_arr = make_list(arr_len)

    shuffled_arr = copy_list(starting_arr)
    random.shuffle(shuffled_arr)

    sorted_arr = my_sort(shuffled_arr)

    print("Shuffled list:", shuffled_arr)
    print("Sorted list:", sorted_arr)

    assert sorted_arr == starting_arr
