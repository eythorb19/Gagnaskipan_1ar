import sys
import os
module_path = os.path.abspath(os.getcwd())    
if module_path not in sys.path:       
    sys.path.append(module_path)

from hangman_pics import *

class UserInterface:
    def __init__(self):
        self.hangman_pics = HangmanPics()
        self.log_in = '''
  _    _          _   _  _____ __  __          _   _ 
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
 |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
                                                                    
                    [1] LOG IN
                    [2] CREATE USER
                    [3] QUIT
'''

        self.main_menu = '''

              
                      _ _             _          
            |\/|  /\   |  |\ |  |\/| |_ |\ | | | 
            |  | /--\ _|_ | \|  |  | |_ | \| |_| 
                                                
--------------------------------------------------------------------
|         [N]ew game    [L]og out    [A]dd words     [S]coreboard  |
--------------------------------------------------------------------
'''
        self.game_type = '''

              G A M E T Y P E 
------------------     ----------------------------
* [D]efault game *     * [P]ick number of guesses *
------------------     ----------------------------
'''   

        self.score_board = '''
                      H I G H S C O R E S                         
-------------------------------------------------------------------
|   Player                  Score          Time                   |
-------------------------------------------------------------------
'''

    def display_menu(self, player, wins, losses, total_score):
        '''Displays main menu'''
        print(self.main_menu)
        print("Player: " + player + "\n")
        print("Games won: " + str(wins))
        print("Games lost: " + str(losses) + "\n")
        print("Total score:" + str(total_score))
        print("__________________________________________")

    def display_misses(self, misses):
        '''Prints out misses'''
        misses_string = "Misses: "
        for i in range(len(misses)):
            misses_string+= misses[i] + ","
        print(misses_string + "\n")

    def display_hangman(self, guess_count,current_string, status, misses = None, score = None):
        '''Displays hangman according to status'''

        print(self.hangman_pics.get_pic(guess_count))
        print(current_string + "\n")
            
        if status == 1:
            print("Nice one, you win!")
            print("Score: " + str(score))

        elif status == 2:
            print("Correct letter.")
            print("Guesses left: " + str(guess_count))

            if len(misses) != 0:
                self.display_misses(misses)

        elif status == 3:
            print("Sorry, wrong letter.")
            print("Guesses left: " + str(guess_count))
            self.display_misses(misses)

        elif status == 0:
            print("Game over")
            print("Score: " + str(score))


    def display_scoreboard(self):
        '''Displays scoreboard.'''
        ordered_list = []

        with open(sys.path[0] + "/scoreboard.txt","r") as file_in:
            file_content = file_in.read()
            score_board = file_content.splitlines()
            file_in.close()

        for i in range(1, len(score_board)):    #Fix output from textfile
            fixed = []
            score_data = (score_board[i]).split(",")
            fixed.append(score_data[0])       #Player
            fixed.append(int(score_data[1]))    #Score
            fixed.append(score_data[2])        #Time
            ordered_list.append(fixed)
        
        ordered_list.sort(key = lambda x: x[1], reverse=True) 
        ordered_list.insert(0,score_board[0])
        print(self.score_board)

        for i in range(1, len(ordered_list)):
            player = ordered_list[i][0]
            score = str(ordered_list[i][1])
            time =  ordered_list[i][2]
            print("|   " + player + self.space_layouting(player, 25)  + score + self.space_layouting(score,15)  + time  +"   |")
        print("\n\n")
        
    def space_layouting(self, word, max):
        '''Space layouting for TUI'''
        string = ""
        for _ in range(max-len(word)):
            string+= " "
        return string

if __name__ == "__main__":
    pass
   
