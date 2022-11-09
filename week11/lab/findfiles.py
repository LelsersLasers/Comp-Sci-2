"""
	Description: Finds and prints all files that match a pattern
	Author: Millan
	Date: 9/20/22
"""

from __future__ import annotations  # type hint support
from os import listdir
from os.path import isdir, expanduser


def find_files(path: str, pattern: str) -> None:
    """
    Purpose: prints all the files that match a pattern
    Parameters: the base path to search from (str), the pattern to match (str)
    Return Val: None
    """
    try: # Question: try is in wrong place?
        files = listdir(path)
        for f in files:
            # check if dir first, so we don't print names of folders
            full_path = path + "/" + f
            if isdir(full_path):
                find_files(full_path, pattern)
            elif pattern in f:
                print(full_path)
    except PermissionError:
        print("Access is denied: '%s'" % path)
    return


def get_path(prompt: str) -> str:
    """
    Purpose: gets a valid path from the user
    Parameters: Prompt (str) is the prompt to display to the user
    Return Val: a valid path that already has '~' expanded (str)
    """
    while True:
        path = input(prompt)
        # Question: expanduser does nothing if "~" not in path,
        #   so there should be no need to check if it is.
        #   This also removes the need for extra string concatenation
        #   and if/try statements.
        expanded_path = expanduser(path)
        if isdir(expanded_path):
            return expanded_path
        else:
            print("No valid directory: '%s' (please enter a valid directory)" % path)


def main():
    expanded_path = get_path("Path   : ")
    pattern = input("Pattern: ")

    print("")
    find_files(expanded_path, pattern)


main()
