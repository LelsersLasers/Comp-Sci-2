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
    try:
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


def get_path() -> str:
    """
    Purpose: gets a valid path from the user
    Parameters: None
    Return Val: a valid path that already has '~' expanded (str)
    """
    while True:
        path = input("Path   : ")
        # does nothing if "~" not in path (so no need to check if it is)
        expanded_path = expanduser(path)
        if isdir(expanded_path):
            return expanded_path
        else:
            print("No valid directory: '%s' (please enter a valid directory)" % path)


def main():
    expanded_path = get_path()
    pattern = input("Pattern: ")

    print("")
    find_files(expanded_path, pattern)


main()
