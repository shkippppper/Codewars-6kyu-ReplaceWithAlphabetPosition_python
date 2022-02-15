

from curses.ascii import isalpha

def alphabet_position(text):

    newText = text.lower()
    SmallerCaseLetters = ["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    newString = ""
    space = " "
    for x in range(len(text)):
        if newText[x].isalpha():
            currentLetter = str(SmallerCaseLetters.index(newText[x]))
            newString = (newString + space + currentLetter)
    return newString.strip()

alphabet_position("The sunset sets at twelve o' clock.")
