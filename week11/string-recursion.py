def isDigit_iterative(S: str) -> bool:
    """Iterative function to verify if string is a number"""
    for char in S:
        if char < "0" or char > "9":
            return False
    return True


def isDigit_recursive(S: str) -> bool:
    """Recursive function to verify if string is a number"""
    if len(S) == 0:
        return True
    elif S[0] < "0" or S[0] > "9":
        return False
    return isDigit_recursive(S[1:])


def isPalindrome_iterative(S: str) -> bool:
    """An iterative function to check whether or not a word is a palindrome"""
    wordLen = len(S)
    for i in range(0, wordLen // 2):  # traverse to the middle character in the word
        beginChar = S[i]  # get 1st, 2nd, 3rd charaters...
        endChar = S[wordLen - i - 1]  # get last, second-to-last, third-to-last chars
        if beginChar != endChar:  # check if opposite characters are the same
            return False  # if they're not, then word is not a palindrome
    return True


def isPalindrome_recursive(S: str) -> bool:
    """A recursive function to check whether or not a word is a palindrome"""
    if len(S) == 0:
        return True
    elif S[0] != S[-1]:
        return False
    return isPalindrome_recursive(S[1:-1])


def main():
    numText = str(input("Enter a number: "))

    if isDigit_iterative(numText) == True:
        print("User entered a number!")
    else:
        print("User did NOT enter a number!")

    if isDigit_recursive(numText) == True:
        print("User entered a number!")
    else:
        print("User did NOT enter a number!")

    if numText.isdigit() == True:
        print("User entered a number!")
    else:
        print("User did NOT enter a number!")

    text = str(input("Enter a string: "))

    if isPalindrome_iterative(text) == True:
        print("String is a palindrome!")
    else:
        print("String is NOT a palindrome!")

    if isPalindrome_recursive(text) == True:
        print("String is a palindrome!")
    else:
        print("String is NOT a palindrome!")


main()
