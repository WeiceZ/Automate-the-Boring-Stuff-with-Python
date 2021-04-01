import re

def isStrongPassword(password):
    eightcharRegex = re.compile(r'(\d|\w|\s){8,}')
    lowercaseRegex = re.compile(r'[a-z]+')
    uppercaseRegex = re.compile(r'[A-Z]+')
    numberRegex = re.compile(r'[0-9]+')

    if eightcharRegex.search(password) == None:
        return False

    if lowercaseRegex.search(password) == None:
        return False

    if uppercaseRegex.search(password) == None:
        return False

    if numberRegex.search(password) == None:
        return False

    return True
