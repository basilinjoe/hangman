import random
import string
from datetime import datetime, timedelta
WORDLIST_FILENAME = "words.txt"


def loadWords():
    print "Loading word list from file..."

    inFile = open(WORDLIST_FILENAME, 'r', 0)

    line = inFile.readline()

    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):

    return random.choice(wordlist)

wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    ns = len(secretWord)
    for a in secretWord:
        if a in lettersGuessed:
            count += 1
    if count == ns:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    b = ''
    for a in secretWord:
        if a in lettersGuessed:
            b += a
        else:
            b += '_'
    return b


def getAvailableLetters(lettersGuessed):

    b = ''
    z="abcdefghijklmnopqrstuvwxyz"
    for a in z:
        if a not in lettersGuessed:
            b += a
    return b


def hangman(secretWord):
    s = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mytime = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    y=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    y= datetime.strptime(y, "%Y-%m-%d %H:%M:%S")
    mytime += timedelta(minutes=1)
    lettersGuessed = []
    flag=0
    al=getAvailableLetters(lettersGuessed)
    guesleft=8
    print "Welcome to the game Hangman!"
    print "you have 5 minutes left "
    print "I am thinking of a word that is ",len(secretWord),"letters long."
    while guesleft>0 and y<mytime:
        y=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        y= datetime.strptime(y, "%Y-%m-%d %H:%M:%S")
        print "-----------"
        print "Time :",y
        print "You have ",guesleft," guesses left."
        print "Available Letters : ",getAvailableLetters(lettersGuessed)
        a=raw_input("Please guess a letter: ").lower()
        al=getAvailableLetters(lettersGuessed)
        if a not in al:
            print "Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed)
            continue
        if a in secretWord:
            lettersGuessed.append(a)
            print "Good guess: ",getGuessedWord(secretWord, lettersGuessed)
            if isWordGuessed(secretWord, lettersGuessed) is True:
                flag=1
                break
        else:
            lettersGuessed.append(a)
            guesleft-=1
            print "Oops! That letter is not in my word: ",getGuessedWord(secretWord, lettersGuessed)
    print "-----------"
    if guesleft==0:
        print"Sorry, you ran out of guesses. The word was ",secretWord
    elif flag==1:
        print "Congratulations, you won!"
    else:
        "Time out"


secretWord = chooseWord(wordlist)
hangman(secretWord)
