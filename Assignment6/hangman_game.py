#/usr/bin/env python3
import sys
import os
import ast
import random

module_path = os.path.abspath(os.getcwd())    
if module_path not in sys.path:       
    sys.path.append(module_path)

from datetime import datetime
from hangman_tui import *

class HangmanGame:
    '''Hangman single game'''
    def __init__(self, player):
        self.word_bank = self.get_word_bank()
        self.current_word = ""
        self.current_string = ""
        self.player = player
        self.guess_count = 7
        self.correct_guess = 0
        self.wrong_guess = 0
        self.total_score = 0
        self.total_guesses = 7
        self.misses = []
        self.tui = UserInterface()

    def get_word_bank(self):
        '''Reads words from txt file and adds to array'''
        with open(sys.path[0] + "/words.txt","r") as file_in:
            file_content = file_in.read()
            words_list = file_content.splitlines()
            file_in.close()
            return words_list

    def new_word(self):
        '''Selects new random word'''
        word = random.choice(self.word_bank)
        self.current_word = word
        self.current_string = self.dash()
        return word

    def check_letter(self, letter):
        '''Check letter'''
        new_current_string = ""
        success = False

        #If user guesses the whole word
        if letter == self.current_word:
            self.tui.display_hangman(self.guess_count, self.current_word, 1)
            self.correct_guess+=1
            self.calculate_score()
            return 1

        #If user guesses letter, check if current word has it
        else:    
            for i in range(len(self.current_word)):
                word_letter = self.current_word[i]  #Get letter in current word
                
                if self.current_string[i] == "-":    #Check if user has guessed the letter before
                    if word_letter == letter:        #Letter is correct
                        new_current_string+=word_letter
                        success = True
                    else:                            #Letter is incorrect                   
                        new_current_string+= "-"
                else:
                    new_current_string+=self.current_string[i]

        #User guesses last letter in word and wins
        if new_current_string == self.current_word:
            self.correct_guess+=1
            self.calculate_score()
            self.tui.display_hangman(self.guess_count, new_current_string, 1, score = self.total_score)
            return 1

        #User guesses correct letter, but not last letter
        elif success == True:
            self.correct_guess+=1
            self.tui.display_hangman(self.guess_count, new_current_string, 2, self.misses)
            self.current_string = new_current_string
            return 2

        #Uses doesn't guess right letter
        else:
            self.guess_count-=1
            self.wrong_guess+=1

            if self.guess_count == 0:   #Last guess used loss
                self.calculate_score()
                self.tui.display_hangman(self.guess_count, self.current_word, 0, score = self.total_score)
                return 0

            else:   #Not last guess
                self.misses.append(letter)
                self.tui.display_hangman(self.guess_count, new_current_string, 3, self.misses)
                return 3

    def dash(self):
        '''Returns dashed word of current word'''
        dash_word = ""
        for _ in range(len(self.current_word)):
            dash_word+= "-"
        return dash_word

    def calculate_score(self):
        '''Calculate game score'''
        max_score = 1000
        wrong_deduct = 40
        correct_letter_deduct = 50/len(self.current_word)

        if self.total_guesses-self.guess_count == 1:
            self.total_score = max_score
        else:
            self.total_score = int(max_score - self.correct_guess*correct_letter_deduct - self.wrong_guess*wrong_deduct-self.total_guesses*10)
        self.store_score()

    def store_score(self):
        '''Store player name, scores and current time to db'''
        now = datetime.now()
        current_time =  now.strftime("%d/%m/%Y %H:%M:%S")
        score_board = open(sys.path[0] + "/scoreboard.txt","a+") 
        scores = self.player.name + "," + str(self.total_score) + "," + current_time + "\n"
        score_board.write(scores) 
        score_board.close() 

if __name__ == "__main__":
    pass