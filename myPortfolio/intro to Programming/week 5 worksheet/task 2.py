"""
Task 2
You will implement a variation of the word game Hangman, if you are unfamiliar with the rules of 
the game, read 
http://en.wikipedia.org/wiki/Hangman_(game).
 
We’re going to start by building some scaffolding that will help you work through the problem.
Grab the hangman.zip file from Learn, it contains 
hangman.py and words.txt,create a ‘hangman’ directory in your portfolio folder and save them both to it. Run hangman.py in the terminal, if you 
have extract the files correctly you should see:

Loading word list from file...
55900 words loaded.

Ultimately, you will implement a function called hangman that will allow the user to play hangman 
against the computer. The computer picks the word and the player tries to guess letters in the word.
This is the general behaviour that needs to be implemented:

1.The computer must select a word at 
random from the list of available words provided by 
words.txt

2.The user is given a certain number of guesses at the beginning of a game.

3.The game is interactive; the user inputs their guess and the computer either:

a.Reveals the letter if it exists in the secret word
b.Penalizes the user and updates the number of guesses remaining

4.The game ends when either the user guesses the secret word or the user runs out of 
guesses.

"""

def hangman():