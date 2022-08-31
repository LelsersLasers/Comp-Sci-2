from __future__ import annotations  # type hint support
from typing import Any  # support for explicit 'Any' type

from sorts import selection_sort


def binary_search(arr: list[Any], element: Any, key = lambda x: x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if key(arr[mid]) == element:
            return mid
        elif key(arr[mid]) > element:
            high = mid - 1
        else:
            low = mid + 1
    return -(mid + 1)


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
    stop_words = get_stop_words(stop_words_filename) # already sorted
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
                        # word_scores.insert(-(idx + 1), [word, score - 2])
                        word_scores.append([word, score - 2])
                        word_scores = selection_sort(word_scores, key = lambda x: x[0])
                    else:
                        word_scores[idx][1] += score - 2
            print("%i/%i = %0.2f" % (i, len(lines), i/len(lines)))
        except ValueError:
            print("Review skipped, incorrect format")
    
    word_scores = selection_sort(word_scores, key = lambda x: x[1], reverse=True)
    return word_scores


def search_for_word(word_scores: list[list[Any]], word: str) -> int:
    for i in range(len(word_scores)):
        if word_scores[i][0] == word:
            return i
    return -1


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
