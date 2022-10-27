"""
	Description: To get movie reviews from a file and check perform sentiment analysis
		on the words in the review, and show the best and worst words. Uses a
        list of lists to store the words and their scores
	Author: Millan
	Date: 10/20/22
"""

from __future__ import annotations  # type hint support
from typing import Any  # support for explicit 'Any' type

import time  # for testing the runtime of the program


def insertion_sort(arr: list[Any], key=lambda x: x, reverse: bool = False) -> None:
    """
    Purpose: Sorts a list (using the Insertion sort algrothrim)
    Parameters: arr (list) the list to be sorted
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
    Parameters: arr (list) of anything to be searched, element (anything) that
        is being searched for in the list, key (function) that is used to get the
        desired value from the list (for example, if the list is a list of lists,
        the key will get the desired value from the list to be searching for). key
        is defaulted to just returning the value without anything special.
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
    Return val: words (list) of the stopwords that were read from the file (sorted)
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
    Parameters: word (str) is the word to check, stopwords (list) is the list of words to ignore
    Return val: True if the word is valid, False otherwise
    """
    return word.isalpha() and binary_search(stopwords, word) < 0


def score_words_in_review(
    items: list[str], word_scores: list[list[Any]], stopwords: list[str]
) -> None:
    """
    Purpose: To score the words in a review
    Parameters: items (list) is the review containing the words and the score,
        word_scores (list) of words and their scores, stopwords (list) is the list
        of words to ignore
    Return val: None
    """
    # items = [score, word1, word2, ...]
    score = int(items[0]) - 2
    review = items[1:]
    for word in review:
        if is_valid_word(word, stopwords):
            # Get index of word in word scores list
            idx = binary_search(word_scores, word, lambda x: x[0])
            if idx < 0:
                # insert where supposed to be if not in list
                word_scores.insert(-idx - 1, [word, score])
            else:
                # otherwise just increase the score
                word_scores[idx][1] += score
    return


def get_word_scores(filename: str, stopwords: list[str]) -> list[list[Any]]:
    """
    Purpose: To read reviews and score words based on the reviews
    Parameters: filename (str) is the name of the file to read the reviews from
                and the words to ignore (list)
    Return val: The scores for each word (unsorted)
    """
    word_scores: list[list[Any]] = []
    with open(filename, "r") as infile:
        for line in infile:
            line = line.strip().lower()
            items = line.split()
            try:
                score_words_in_review(items, word_scores, stopwords)
            except:
                print("Review skipped, incorrect format")
    return word_scores


def print_word_score(word_score: list[Any]) -> None:
    """
    Purpose: Displays the scores and the word to the console
    Parameters: word_score (list) which contains the word (str) and the score (int)
    Return val: None
    """
    print("%3i\t%s" % (word_score[1], word_score[0]))
    return


def display_word_scores(word_scores: list[list[Any]], number_to_display: int) -> None:
    """
    Purpose: To format how the scores of the words are displayed
    Parameters: a list of lists which contains a word (str) and a score (int)
    Return val: None
    """
    if len(word_scores) < number_to_display * 2:
        print("All word scores:")
        for word_score in word_scores:
            print_word_score(word_score)
    else:
        print("Top 20")
        for word_score in word_scores[:number_to_display]:
            print_word_score(word_score)
        print("\nBottom 20")
        for word_score in word_scores[-number_to_display:]:
            print_word_score(word_score)
    return


def main():

    start_time = time.time()

    # reads in the words to ignore (pre sorted)
    stopwords = read_stopwords("stopwords.txt")

    # reads reviews and scores words based on the reviews
    word_scores = get_word_scores("movieReviews.txt", stopwords)

    # sorts the words based on their scores
    insertion_sort(word_scores, key=lambda x: x[1], reverse=True)

    # displays the words and their scores
    display_word_scores(word_scores, 20)

    elapsed_time = time.time() - start_time
    print("\n\nElapsed time: %.2f seconds" % elapsed_time)


main()
