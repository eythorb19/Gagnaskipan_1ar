#/usr/bin/env python3
import csv
from csv import writer
from csv import reader

import sys
import os
module_path = os.path.abspath(os.getcwd())    
if module_path not in sys.path:       
    sys.path.append(module_path)

class User:
    '''User with name, wins, losses and total score'''
    def __init__(self, name = None, wins = 0, losses = 0, total_score = 0):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.total_score = total_score

class ManageUsers:
    '''Functions to manage users'''

    def store_user(self, user):
        '''Stores user to csv'''
        with open(sys.path[0] + "/users.csv", 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow([user.name, user.wins, user.losses, user.total_score])

    def check_if_user_exists(self, username):
        '''Checks if user exists'''
        users = self.read_users()
        for i in range(1, len(users)):
            if users[i][0] == username:
                return True 
        return False
    
    def get_user(self, username):
        '''Returns user'''
        users = self.read_users()

        for i in range(1, len(users)):
            if users[i][0] == username:
                player = users[i][0]
                wins = int(users[i][1])
                losses = int(users[i][2])
                total_score = int(users[i][3])
                user = User(player, wins, losses, total_score)
                return user

    def read_users(self):
        '''Read users'''
        with open(sys.path[0] + "/users.csv", 'r') as read_obj:
            csv_reader = reader(read_obj)
            list_of_rows = list(csv_reader)
        return list_of_rows

    def update_user(self, user_name, wins, losses, total_score):
        '''Updates information about user'''
    
        #Writes lines that doesn't have the users name into array
        lines = list()
        with open(sys.path[0] + "/users.csv", 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row[0] != user_name:
                    lines.append(row)
        #Writes out lines
        with open(sys.path[0] + "/users.csv", 'w',newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        #Appends new user info
        user = User(user_name, wins, losses, total_score)
        self.store_user(user)

if __name__ == "__main__":
    pass
