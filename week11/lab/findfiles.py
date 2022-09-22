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
        path = expanduser(path)
        for file in listdir(path):
            # check if dir first, so we don't print names of folders
            if isdir(path + "/" + file):
                find_files(path + "/" + file, pattern)
            elif pattern in file:
                print(path + "/" + file)
    except PermissionError:
        print("Access is denied: '%s'" % path)
    except FileNotFoundError:
        print("The system cannot find the path specified: '%s'" % path)


def main():
    path = input("Path   : ")
    pattern = input("Pattern: ")

    print("")
    find_files(path, pattern)


main()
