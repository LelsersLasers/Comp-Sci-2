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
    Purpose: Sorts a list (Note: same as insertion_sort)
    Parameters: arr (list) the list to be sorted
    Return val: A copy of the sorted list
    """
    new_arr = copy_list(arr)
    for i in range(len(new_arr) - 1):
        lowest_idx = len(new_arr) - 1
        for j in range(i, len(new_arr) - 1):
            if new_arr[j] < new_arr[lowest_idx]:
                lowest_idx = j
        lowest = new_arr.pop(lowest_idx)
        new_arr.insert(i, lowest)
    return new_arr


def bubble_sort(arr: list[Any]) -> list[Any]:
    """
    This is the bubble sort algorithm:
        - given a list arr
        - for every item in the list, compare to the item just to the right, swap if needed
        - keep doing the above until you go from one end of the list to the
          other and don't make any swaps!
    Purpose: Sorts a list (using the BubbleSort algrothrim)
    Parameters: arr (list) the list to be sorted
    Return val: A copy of the sorted list
    """
    new_arr = copy_list(arr)
    for i in range(len(new_arr)):
        for j in range(len(new_arr) - i - 1):
            if new_arr[j] > new_arr[j + 1]:
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
    return new_arr


def insertion_sort(arr: list[Any]) -> list[Any]:
    """
    This is the insertion sort algorithm:
        - assume item at index 0 is already "sorted"
        - starting with item at index 1, check all items to the left and swap positions if needed
        - do the same for item at index 2, where now items at index 0 and 1 should be in order
        - do the same for item at index 3, where now items at index 0, 1, and 2 are in order...and so on

    NOTE: Notice that, for each index, all items to the left are in order, and you are inserting the next item into the correct spot.
    Purpose: Sorts a list (using the Insertion sort algrothrim)
    Parameters: arr (list) the list to be sorted
    Return val: A copy of the sorted list
    """
    new_arr = copy_list(arr)
    for i in range(len(new_arr) - 1):
        lowest_idx = len(new_arr) - 1
        for j in range(i, len(new_arr) - 1):
            if new_arr[j] < new_arr[lowest_idx]:
                lowest_idx = j
        lowest = new_arr.pop(lowest_idx)
        new_arr.insert(i, lowest)
    return new_arr


def selection_sort(arr: list[Any]) -> list[Any]:
    """
    This is the selection sort algorithm:
        - given a list L
        - find the smallest number in the list, swap it to position 0
        - find the next smallest number in the list, swap it to position 1
        - find the next smallest number in the list, swap it to position 2
        - And so on...

    NOTE: It is called selection sort because, each time, you are selecting
    the smallest number from the remaining unsorted elements.
    Purpose: Sorts a list (using the Selection sort algrothrim)
    Parameters: arr (list) the list to be sorted
    Return val: A copy of the sorted list
    """
    new_arr = copy_list(arr)
    for i in range(len(new_arr) - 1):
        lowest_idx = len(new_arr) - 1
        for j in range(i, len(new_arr) - 1):
            if new_arr[j] < new_arr[lowest_idx]:
                lowest_idx = j
        new_arr[lowest_idx], new_arr[i] = new_arr[i], new_arr[lowest_idx]
    return new_arr


def jerry_sort(arr: list[Any], low: int, high: int) -> None:
    """
    Purpose: Sorts a section of a list (based on Jerry's incorrect yet working interpertation of the Quick sort algrothrim)
    Parameters: arr the list to be sorted, low the left bound of the section, high the right bound
    Return val: None (it modifies the input list)
    """
    split = low
    if low < high:
        for i in range(low + 1, high + 1):
            if arr[i] < arr[low]:
                arr[low], arr[i] = arr[i], arr[low]

        arr[low], arr[split] = arr[split], arr[low]
        jerry_sort(arr, low, split - 1)
        jerry_sort(arr, split + 1, high)


def jerry_sort_full(arr: list[Any]) -> list[Any]:
    """
    Purpose: Sorts a list (using the Jerry's incorrect yet working interpertation of the QUick sort algrothrim)
    Parameters: arr (list) the list to be sorted
    Return val: A copy of the sorted list
    Note: hits maximum recursion depth fairly quickly
    """
    new_arr = copy_list(arr)
    jerry_sort(new_arr, 0, len(new_arr) - 1)
    return new_arr


def python_sort(arr: list[Any]) -> list[Any]:
    """
    Purpose: Sorts a list (using python's built-in sort())
    Parameters: arr (list) the list to be sorted
    Return val: A copy of the sorted list
    """
    return sorted(arr)


def time_sorts(arr_len: int, sorts: list) -> list[float]:
    """
    Purpose: Time a sorting function/implementation
    Parameters: The length of the list to test (int), and a list of sorting functions to use
    Return val: A list of the times it took for all the sorts to sort the same shuffled list (-1 if a sort did not work)
    """
    import time  # for timing the sort
    import random  # for shuffle

    starting_arr = make_list(arr_len)

    shuffled_arr = copy_list(starting_arr)
    random.shuffle(shuffled_arr)

    times: list[float] = []

    for sort in sorts:
        start_time = time.time()
        sorted_arr = sort(shuffled_arr)
        time_taken = time.time() - start_time

        if sorted_arr != starting_arr:
            times.append(-1)
        times.append(time_taken)

    return times


if __name__ == "__main__":

    arr_len = 10000

    sorts = [my_sort, bubble_sort, insertion_sort, selection_sort]
    sort_names = ["My sort", "Bubble sort", "Insertion sort", "Selection sort"]
    times = time_sorts(arr_len, sorts)

    print("Array length: %i" % arr_len)
    for i in range(len(sorts)):
        print("%s time:\t%.2f seconds" % (sort_names[i], times[i]))
