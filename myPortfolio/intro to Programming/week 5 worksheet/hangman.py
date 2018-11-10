


import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):

    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):

    secret_word = 'apple'
    letters_guessed = ['_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    print(is_word_guessed(secret_word, letters_guessed)

def get_guessed_word(secret_word, letters_guessed):

    secret_word = 'apple'
    letters_guessed = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    print(get_guessed_word)secret_word, letters_guessed))

def get_available_letters(letters_guessed):
    
    print(string.ascii_lowercase) # <-- ?
    letters_guessed:['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    print(get_available_letters(letters_guessed))
    

def hangman(secret_word):

    secret_word = choose_word(wordlist)
    hangman(secret_word)
"""
    print("Welcome to the game Hangman!")
    print("I am thinking of a word ...")
    print("you have", guesses, "remaining.")
    print("Available letters:",string.ascii_lowercase)
    letters_guessed=input("Please guess a letter: )        
    print("Good guess:") _ a _ _
    print("you have", guesses, "remaining.")
    print("Available letters:",string.ascii_lowercase)
    letters_guessed=input("Please guess a letter:)
    print("oops! That letter is not in my word:")
    print("You have 3 warnings left")
    print("You have 6 guesses left")
    print("Congratulations, you won!")
    print("Your total score for this game is: ")
    print("Sorry, you ran out of guesses. the word was...")
"""




