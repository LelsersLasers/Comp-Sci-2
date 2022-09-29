"""
    Description: This program gets the name of a python file from its user,
    			 goes through the file line by line, and determines whether
				 there are any lines that contain unbalanced parentheses.
    Author: Millan
    Date: 9/28
"""

from __future__ import annotations  # type hint support


#------------------------------------------------------------------------------#
def isBalancedHelper(line: str, count: int) -> bool:
    """ Recursively examine the characters in the string from left to right,
        while keeping track of how many open parentheses have not yet been closed.
        If unclosed paren counter ever becomes negative, you have unbalanced parens.
    """
    # your recursive code goes here
    if len(line) == 0:
        return count == 0
    else:
        if line[0] == "(":
            count += 1
        elif line[0] == ")":
            count -= 1
        if count < 0:
            return False
        else:
            return isBalancedHelper(line[1:], count)

#------------------------------------------------------------------------------#
def isBalanced(line: str) -> bool:
    """
    Purpose: determine if a single line from the file has balanced parentheses
    Parameters: a line from the file (string)
    Return Val: a boolean indicating whether the line has balanced parens
    """
    # set initial unclosed parens count to 0 & delegate work to recursive function
    return isBalancedHelper(line, 0)

#------------------------------------------------------------------------------#
def main():

	# get the name of a python file from its user
    filename = input("Enter file name: ")
    
    no_issues = True
    # read file line by line and determine whether there are any w/ unbalanced parens
    with open(filename, 'r') as file:
        line_number = 1
        for line in file:
            line = line.strip()
            if not isBalanced(line):
                print("Unbalanced parentheses on line %i of %s" % (line_number, filename))
                print("\t%s" % line)
                no_issues = False
            line_number += 1
    
    if no_issues:
        print("File %s has no unbalanced parentheses" % filename)



main()
