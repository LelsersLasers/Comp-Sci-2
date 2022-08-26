from __future__ import annotations  # type hint support
from typing import Any  # support for explicit 'Any' type


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


def get_movie_reviews(filename: str) -> list[list[Any]]:
    lines = read_file(filename)
    movie_reviews = []
    for line in lines:
        try:
            items = line.split()
            score = int(items[0])
            movie_reviews.append([score, items[1:]])
        except ValueError:
            print("Review skipped, incorrect format")
    return movie_reviews


def score_movie_reviews(
    movie_reviews: list[list[Any]], stop_words: list[str]
) -> list[list[Any]]:
    word_scores = []
    for review in movie_reviews:
        for word in review[1]:
            word = word.lower()
            if word.isalpha() and not word in stop_words:  # TODO: change in to binary
                idx = search_for_word(word_scores, word)
                if idx == -1:
                    word_scores.append([word, review[0] - 2])
                else:
                    word_scores[idx][1] += review[0] - 2

    word_scores.sort(key=lambda x: x[1], reverse=True)
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
        print("Best 20 words:")
        for word_score in word_scores[:20]:
            print_word_score(word_score)
        print("Worst 20 words:")
        for word_score in word_scores[-20:]:
            print_word_score(word_score)


if __name__ == "__main__":
    stop_words = get_stop_words("stopwords.txt")
    movie_reviews = get_movie_reviews("movieReviews.txt")
    word_scores = score_movie_reviews(movie_reviews, stop_words)
    display_word_scores(word_scores)
