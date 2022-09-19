from __future__ import annotations  # type hint support
# from typing import Any  # support for explicit 'Any' type

from os import listdir
from os.path import isdir, expanduser



def find_files(path: str, pattern: str) -> None:
    try:
        for file in listdir(path):
            if pattern in file:
                print(path + file)
            if isdir(file):
                find_files(file, pattern)
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