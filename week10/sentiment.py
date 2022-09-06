"""
	Description: To get movie reviews from a file and check perform sentiment analysis
		on the words in the review, and show the best and worst words
	Author: Jerry and Millan
	Date: 9/6/22
"""

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
	Purpose: Sorts a list (using the Insertion sort algrothrim)
	Parameters: arr (list) the list to be sorted
	Return val: A copy of the sorted list

	This is the insertion sort algorithm:
		- assume item at index 0 is already "sorted"
		- starting with item at index 1, check all items to the left and swap positions if needed
		- do the same for item at index 2, where now items at index 0 and 1 should be in order
		- do the same for item at index 3, where now items at index 0, 1, and 2 are in order...and so on
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
	"""
	Purpose: Finds the desired value in a list
	Parameters: arr (list) of anything to be searched, element (anything) that
		is being searched for in the list, key (function) that is used to get the
		desired value from the list (for example, if the list is a list of lists,
		the key will get the desired value from the list to be searching for). key
		is defaulted to just returning the value without anything special.
	Return val: the index (int) of the found value, or the negative index of the
		location that the value is supposed to be at
	"""
	low = 0
	high = len(arr) - 1 			  # Get boundary indexes
	while low <= high:				  # Continue searching until item not in list
		mid = (low + high) // 2		  # Calculate the middle value within boundaries
		if key(arr[mid]) == element:  # If desired value is found, return the index
			return mid
		elif key(arr[mid]) > element: # If the value is smaller, move the boundaries
			high = mid - 1			  # to the left of the middle index
		else:						  # otherwise move the boundaries to the right
			low = mid + 1			  # of the middle index
	return -(low + 1)				  # return -(insertion point + 1)


def read_file(filename: str) -> list[str]:
	"""
	Purpose: To read the lines from a text file
	Parameters: Filename (str) is the name of the file that the function should
		read data from
	Return val: lines (list) of the lines from the file that were read into the
		program
	"""
	lines = []
	with open(filename, "r") as file:	# open the file
		for line in file:				# loop through the lines in the file
			line = line.strip().lower() # get rid of whitespace and capital letters
			lines.append(line)			# add line to list of lines
	return lines						# return lines


def get_stop_words(filename: str) -> list[str]:
	"""
	Purpose: To get the stopwords from a file
	Parameters: Filename (str) is the file to get the stopwords from
	Return val: words (list of strings) is the list of stop words that the program
		will use, which is sorted alphabetically
	"""
	lines = read_file(filename) # Get stopwords
	words = []
	for line in lines:
		if line.isalpha():		# if the line is only alphabet characters
			words.append(line)	# add to list
	return words				# return list


def get_word_scores(reviews_filename: str, stop_words_filename: str) -> list[list[Any]]:
	"""
	Purpose: Gets the reviews and scores the words based on the review score
	Parameters: the files names (str) are the names of the files to get reviews
		and stop words from
	Return val: list of list of the word (str) and the score of the word (int) which
		is sorted alphabetically
	"""
	lines = read_file(reviews_filename)				  # get reviews
	stop_words = get_stop_words(stop_words_filename)  # get sorted stopwords
	word_scores: list[list[Any]] = []				  # list of lists of words and score
	for line in lines:
		try:										  # if review is formatted correctly
			items = line.split()					  # get each word
			score = int(items[0])					  # get score of review
			for word in items[1:]:					  # loop through word in review
				word = word.lower()
				# if the word is alphabet and is not a stopword
				if word.isalpha() and binary_search(stop_words, word) < 0:
					idx = binary_search(word_scores, word, lambda x: x[0])
					if idx < 0:
						word_scores.insert(-idx - 1, [word, score - 2])
					else:
						word_scores[idx][1] += score - 2
		except ValueError:							  # Skip review if not formatted
			print("Review skipped, incorrect format") # correctly

	word_scores = insertion_sort(word_scores, key=lambda x: x[1], reverse=True)
	return word_scores


def print_word_score(word_score: list[Any]) -> None:
	"""
	Purpose: Displays the scores and the word to the console
	Parameters: word_score (list) which contains the word (str) and the score (int)
	Return val: None
	"""
	print("%3i\t%s" % (word_score[1], word_score[0]))


def display_word_scores(word_scores: list[list[Any]]) -> None:
	"""
	Purpose: To format how the scores of the words are displayed
	Parameters: a list of lists which contains a word (str) and a score (int)
	Return val: None
	"""
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
