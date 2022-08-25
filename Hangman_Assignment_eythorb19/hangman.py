#/usr/bin/env python3
import sys
import os
module_path = os.path.abspath(os.getcwd())    
if module_path not in sys.path:       
    sys.path.append(module_path)
import random
import ast
from datetime import datetime

from hangman_tui import *
from hangman_app import *
from user import *

class MainMenu:
    '''Main menu for Hangman game'''
    def __init__(self):
        self.tui = UserInterface()
        self.start()
        self.player = None

    def login(self, user_name):
        '''Log in user'''
        users = ManageUsers()
        self.player = users.get_user(user_name)
        self.display_menu()

    def create_user(self, user_name):
        '''Create user'''
        users = ManageUsers()
        self.player = User(user_name)
        users.store_user(self.player)
        self.display_menu()

    def start(self):
        '''Log in for hangman game'''
        print(self.tui.log_in)
        users = ManageUsers()
        login = input("Insert 1,2 or 3 and press enter: ")

        if login == "1":
            print("LOG IN USER")
            user_name = input("Insert username: ")
            exists = users.check_if_user_exists(user_name)
            
            if exists == True:
                self.login(user_name),
            else:
                print("User doesn't exist.")
                input("Press enter to go back.")
                self.start()
        elif login == "2":
            print("CREATING NEW USER")
            user_name = input("Insert username:")
            exists = users.check_if_user_exists(user_name)
            
            if exists == True:
                input("User exists. Press enter to go back")
                self.start()
            else:
                self.create_user(user_name)

        elif login == "3":
            return
        else:
            self.start()
                    
    def add_words(self):
        '''Add new word to database'''
        new_word = input("What word do you want to add to list of available hangman words? \n")
        try:
            words_list = open(sys.path[0] + "/words.txt","a+") 
            words_list.write("\n" +new_word) 
            words_list.close() 
            print("New word was added successfully.")
            input("\n\nPress enter to go back to the main menu.")
            self.display_menu()
        except:
            print("404, Could not add the word to database.")
        self.display_menu

    def select_game_type(self, app):
        '''Selects default game - or user chooses to change number of guesses'''
        set_guess = input("Insert D or P.\n").upper()

        if set_guess == "P":
            self.change_guesses(app)

        elif set_guess != "D":
            print("Wrong input.")
            self.select_game_type(app)
        return
    
    def change_guesses(self, app):
        '''Allows user to change guesses'''

        try:
            number_input = int(input("How many guesses do you want to have?"))

            if number_input > 25:
                print("The max number of guesses is 25, since there are 25 letters in the alphabet.")
                self.change_guesses(app)
            else:
                app.hangman.guess_count = number_input
                app.hangman.total_guesses = number_input
            return
        
        except: 
            print("Invalid input. Try again.")
            self.change_guesses(app)

    def display_menu(self):
        '''Display Main menu'''
        self.tui.display_menu(self.player.name, self.player.wins, self.player.losses, self.player.total_score)
        selection = input("Choose N, L, A or S, and press enter: ").upper()
        self.select(selection)

    def select(self, selection):
        '''Select where to go from main menu'''
        if selection == "N":  #New Hangman Game
            app = hangmanApp(self.player) #Start the app
            print(self.tui.game_type)
            self.select_game_type(app)   #Select number of guesses
            game_status = app.new_game()    #Start new game

            #Game won
            if game_status == 1:
                self.player.wins+=1
                self.player.total_score+= app.hangman.total_score
                input("\n\nPress enter to go back to the main menu.")
                self.display_menu()

            #Game lost
            elif game_status == 0:
                self.player.losses+=1
                self.player.total_score+= app.hangman.total_score
                input("\n\nPress enter to go back to the main menu.")
                self.display_menu()       

        elif selection == "L": #Quit program
            users = ManageUsers()
            users.update_user(self.player.name, self.player.wins, self.player.losses, self.player.total_score)
            self.start()

        elif selection == "A":  #Add more words to collection
            self.add_words()
        elif selection =="S":   #Display scoreboard
            self.tui.display_scoreboard()
            input("Press Enter to go back to the main menu")
            self.display_menu()
        else: 
            self.display_menu()

if __name__ == "__main__":
    startHangman = MainMenu()