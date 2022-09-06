from __future__ import annotations  # type hint support
from typing import Any  # support for explicit 'Any' type


def copy_list(arr: list[Any]) -> list[Any]:
    """
    Purpose: Copies a list
    Parameters: arr (list) the list to copy
    Return val: The copied list
    """
    return [x for x in arr]

def insertion_sort(arr: list[Any], key=lambda x: x, reverse: bool = False) -> list[Any]:
    """
    This is the insertion sort algorithm:
        - assume item at index 0 is already "sorted"
        - starting with item at index 1, check all items to the left and swap positions if needed
        - do the same for item at index 2, where now items at index 0 and 1 should be in order
        - do the same for item at index 3, where now items at index 0, 1, and 2 are in order...and so on
    Purpose: Sorts a list (using the Insertion sort algrothrim)
    Parameters: arr (list) the list to be sorted
    Return val: A copy of the sorted list
    """
    new_arr = copy_list(arr)
    for i in range(1, len(new_arr)):
        val = new_arr[i]
        j = i - 1
        while j >= 0 and key(val) < key(new_arr[j]):
            new_arr[j + 1] = new_arr[j]
            j -= 1
        new_arr[j + 1] = val
    if reverse:
        return list(reversed(new_arr))
    return new_arr


def binary_search(arr: list[Any], element: Any, key=lambda x: x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if key(arr[mid]) == element:
            return mid
        elif key(arr[mid]) > element:
            high = mid - 1
        else:
            low = mid + 1
    return -(low + 1)


def read_file(filename: str) -> list[str]:
    lines = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip().lower()
            lines.append(line)
    return lines


def get_stop_words(filename: str) -> list[str]:
    lines = read_file(filename)
    words = []
    for line in lines:
        if line.isalpha():
            words.append(line)
    return words


def get_word_scores(reviews_filename: str, stop_words_filename: str) -> list[list[Any]]:
    lines = read_file(reviews_filename)
    stop_words = get_stop_words(stop_words_filename)  # already sorted
    word_scores: list[list[Any]] = []
    i = 0
    for line in lines:
        i += 1
        try:
            items = line.split()
            score = int(items[0])
            for word in items[1:]:
                word = word.lower()
                if word.isalpha() and binary_search(stop_words, word) < 0:
                    idx = binary_search(word_scores, word, lambda x: x[0])
                    if idx < 0:
                        word_scores.insert(-idx - 1, [word, score - 2])
                    else:
                        word_scores[idx][1] += score - 2
        except ValueError:
            print("Review skipped, incorrect format")

    word_scores = insertion_sort(word_scores, key=lambda x: x[1], reverse=True)
    return word_scores


def print_word_score(word_score: list[Any]) -> None:
    print("%3i\t%s" % (word_score[1], word_score[0]))


def display_word_scores(word_scores: list[list[Any]]) -> None:
    if len(word_scores) < 40:
        print("All word scores:")
        for word_score in word_scores:
            print_word_score(word_score)
    else:
        print("Top 20")
        for word_score in word_scores[:20]:
            print_word_score(word_score)
        print("\nBottom 20")
        for word_score in word_scores[-20:]:
            print_word_score(word_score)


if __name__ == "__main__":
    word_scores = get_word_scores("movieReviews.txt", "stopwords.txt")
    display_word_scores(word_scores)
