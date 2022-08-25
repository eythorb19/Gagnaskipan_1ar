#/usr/bin/env python3
import sys
import os
import ast
module_path = os.path.abspath(os.getcwd())    
if module_path not in sys.path:       
    sys.path.append(module_path)
import random
from datetime import datetime
from hangman_pics import *
from hangman_game import *

class hangmanApp:
    '''Hangman app'''
    def __init__(self, player):
        self.hangman = HangmanGame(player)
        self.current_word = ""
        self.hangman_pics = HangmanPics()
        self.guess_list = []

    def new_game(self):
        '''Starts a new hangman game'''
        self.current_word = self.hangman.new_word()
        dashed_word = self.hangman.dash()
        print(self.hangman_pics.get_pic(6))
        print(dashed_word)
        print("Guesses left: " + str(self.hangman.guess_count))
        return self.guess()

    def guess(self):
        '''Asks the user to guess a letter recursively until game is won or lost'''
        letter = input("Make a guess, 1 letter or whole word!\n").lower()
        for i in range(len(self.guess_list)):
            if letter == self.guess_list[i]:
                print("You've already guessed this letter.")
                return self.guess()

        self.guess_list.append(letter)
        guess = self.hangman.check_letter(letter)

        if guess == 0 or guess == 1:
            return guess
        else:
            check = self.guess()
            return check

if __name__ == "__main__":
    pass
   