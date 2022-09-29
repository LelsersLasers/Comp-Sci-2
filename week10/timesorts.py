"""
    Description: Time multiple sorting algrothrims/implementations
    Author: Millan
    Date: 8/30/22
"""

from __future__ import annotations  # type hint support
from typing import Any  # support for explicit 'Any' type

from sorts import *


def time_sorts(base_arr_len: int, doubles: int, sorts: list) -> list[list[float]]:
    """
    Purpose: Time a sorting function/implementation
    Parameters: The length of the list to test (int), how many times to time each sort
        where each set, the length doubles(int), and a list of sorting functions to use
    Return val: A list of the times it took for all the sorts to sort the same
        shuffled list (-1 if a sort did not work)
    """
    import time  # for timing the sort
    import random  # for shuffle

    times: list[list[float]] = []

    for multiplier in range(0, doubles):

        starting_arr = make_list(base_arr_len * 2 ** multiplier)

        shuffled_arr = copy_list(starting_arr)
        random.shuffle(shuffled_arr)

        times_for_len: list[float] = []

        for sort in sorts:
            start_time = time.time()
            sorted_arr = sort(shuffled_arr)
            time_taken = time.time() - start_time

            if sorted_arr != starting_arr:
                times_for_len.append(-1)
            else:
                times_for_len.append(time_taken)

        times.append(times_for_len)

    return times


def get_positive_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a positive integer.")
            continue


def get_input() -> tuple[int, int]:
    """
    SOME GREAT COMMENT
    """
    arr_len = get_positive_int("N: ")
    doubles = get_positive_int("Times to double: ")
    return arr_len, doubles


if __name__ == "__main__":

    arr_len, doubles = get_input()

    sorts = [my_sort, bubble_sort, insertion_sort, selection_sort, merge_sort_full, python_sort]
    sort_names = ["My sort", "Bubble sort", "Insertion sort", "Selection sort", "Merge sort", "Python sort",]
    times = time_sorts(arr_len, doubles, sorts)

    for multiplier in range(0, doubles):
        print("\nArray length: %i" % (arr_len * 2 ** multiplier))
        for i in range(len(sorts)):
            print("%15s time:\t%.3f seconds" % (sort_names[i], times[multiplier][i]))