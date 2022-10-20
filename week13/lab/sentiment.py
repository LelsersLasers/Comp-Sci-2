"""
	Description: To get movie reviews from a file and check perform sentiment analysis
		on the words in the review, and show the best and worst words
	Author: Millan
	Date: 10/20/22
"""

from __future__ import annotations  # type hint support
from typing import Any  # support for explicit 'Any' type


def insertion_sort(arr: list[Any], key=lambda x: x, reverse: bool = False) -> None:
    """
    Purpose: Sorts a list (using the Insertion sort algrothrim)
    Parameters: arr (list) that is sorted, key (optional function) a transform
		to be applied when comparing values, reverse (optional bool) sort descending or ascending
    Return val: None

    This is the insertion sort algorithm:
    - assume item at index 0 is already "sorted"
    - starting with item at index 1, check all items to the left and swap positions if needed
    - do the same for item at index 2, where now items at index 0 and 1 should be in order
    - do the same for item at index 3, where now items at index 0, 1, and 2 are in order...and so on
    """
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and key(val) < key(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val
    if reverse:
        arr.reverse()
    return


def binary_search(arr: list[Any], element: Any, key=lambda x: x):
    """
    Purpose: Finds the desired value in a list
    Parameters: arr (list) to be searched, element (Any) that is being searched for in the
        list, key (optional function) a transform applied to the items in the list but not
		the element being search for
    Return val: the index (int) of the found value, or the negative index of the insertion point + 1
    """
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
    return -(low + 1)  # return -(insertion point + 1)


def read_stopwords(filename: str) -> list[str]:
    """
    Purpose: To read the stopwords from a file
    Parameters: filename (str) is the name of the file to read the stopwords from
    Return val: words (list) of the stopwords that were read from the file (already sorted)
    """
    stopwords = []
    with open(filename, "r") as infile:
        for line in infile:
            line = line.strip().lower()
            if line.isalpha():
                stopwords.append(line)
    return stopwords


def get_word_scores(filename: str, stopwords: list[str]) -> dict[str, int]:
    """
    Purpose: To read reviews and score words based on the reviews
    Parameters: filename (str) is the name of the file to read the reviews from
        and the words to ignore (list)
    Return val: The scores for each word (dict with keys=words and values=scores)
    """
    word_scores: dict[str, int] = {}
    with open(filename, "r") as infile:
        for line in infile:
            line = line.strip().lower()
            items = line.split()
            try:
                score = int(items[0]) - 2
                review = items[1:]
                for word in review:
                    # Is valid word
                    if word.isalpha() and binary_search(stopwords, word) < 0:
                        try:
                            word_scores[word] += score
                        except KeyError:
                            word_scores[word] = score
            except:
                print("Review skipped, incorrect format")
    return word_scores


def print_word_score(word_score: tuple[str, int]) -> None:
    """
    Purpose: Displays the scores and the word to the console
    Parameters: word_score (tuple) which contains the word (str) and the score (int)
    Return val: None
    """
    print("%3i\t%s" % (word_score[1], word_score[0]))
    return


def display_word_scores(
    word_score_tuples: list[tuple[str, int]], number_to_display: int
) -> None:
    """
    Purpose: To format how the scores of the words are displayed
    Parameters: a list of lists which contains a word (str) and a score (int)
    Return val: None
    """
    if len(word_score_tuples) < number_to_display * 2:
        print("All word scores:")
        for word_score in word_score_tuples:
            print_word_score(word_score)
    else:
        print("Top 20")
        for word_score in word_score_tuples[:number_to_display]:
            print_word_score(word_score)
        print("\nBottom 20")
        for word_score in word_score_tuples[-number_to_display:]:
            print_word_score(word_score)
    return


def main():

    # reads in the words to ignore (pre sorted)
    stopwords = read_stopwords("stopwords.txt")

    # reads reviews and scores words based on the reviews
    word_scores = get_word_scores("movieReviews.txt", stopwords)

    # sorts the words based on their scores
    word_score_tuples = list(word_scores.items()) # list[tuple[word, score]]
	# lambda item: item[1] = sort based on score; reverse=True = sort descending
    insertion_sort(word_score_tuples, key=lambda item: item[1], reverse=True)

    # displays the words and their scores
    display_word_scores(word_score_tuples, 20)


main()
