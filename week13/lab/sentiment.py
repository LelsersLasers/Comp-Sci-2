"""
	Description: To get movie reviews from a file and check perform sentiment
        analysis on the words in the review, and show the best and worst words.
        Uses a dictionary to store the words and their scores.
	Author: Millan
	Date: 10/20/22
"""

from __future__ import annotations  # type hint support
from typing import Any  # support for explicit 'Any' type

import time  # for testing the runtime of the program


def insertion_sort(arr: list[Any], key=lambda x: x, reverse: bool = False) -> None:
    """
    Purpose: Sorts a list (using the Insertion sort algrothrim)
    Parameters: arr (list) that is sorted, key (optional function) a transform
        to be applied when comparing values, reverse (optional bool) sort descending
        or ascending
    Return val: None
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
    Parameters: arr (list) to be searched, element (Any) that is being searched
        for in the list, key (optional function) a transform applied to the items
        in the list but not the element being searched for
    Return val: the index (int) of the found value, or the negative index of the
        insertion point + 1
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
    Return val: words (list) of the stopwords that are already sorted
    """
    stopwords = []
    with open(filename, "r") as infile:
        for line in infile:
            line = line.strip().lower()
            if line.isalpha():
                stopwords.append(line)
    return stopwords


def is_valid_word(word: str, stopwords: list[str]) -> bool:
    """
    Purpose: To check if a word is valid
    Parameters: word (str) is the word to check, stopwords (list) is the list of
        words to ignore
    Return val: True if the word is valid, False otherwise
    """
    return word.isalpha() and binary_search(stopwords, word) < 0


def score_words_in_review(
    items: list[str], word_scores: dict[str, int], stopwords: list[str]
) -> None:
    """
    Purpose: To score the words in a review
    Parameters: items (list) of the review containing the words and the score,
        word_scores (dict) is the dictionary of words and their scores, stopwords
        (list) is the list of words to ignore
    Return val: None
    """
    # items = [score, word1, word2, ...]
    score = int(items[0]) - 2
    review = items[1:]
    for word in review:
        if is_valid_word(word, stopwords):
            try:
                word_scores[word] += score
            except KeyError:
                word_scores[word] = score
    return


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
                score_words_in_review(items, word_scores, stopwords)
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

    start_time = time.time()

    # reads in the words to ignore (pre sorted)
    stopwords = read_stopwords("stopwords.txt")

    # reads reviews and scores words based on the reviews
    word_scores = get_word_scores("movieReviews.txt", stopwords)

    # sorts the words based on their scores
    word_score_tuples = list(word_scores.items())  # list[tuple[word, score]]
    # lambda item: item[1] = sort based on score; reverse=True = sort descending
    insertion_sort(word_score_tuples, key=lambda item: item[1], reverse=True)

    # displays the words and their scores
    display_word_scores(word_score_tuples, 20)

    elapsed_time = time.time() - start_time
    print("\n\nElapsed time: %.2f seconds" % elapsed_time)


main()
