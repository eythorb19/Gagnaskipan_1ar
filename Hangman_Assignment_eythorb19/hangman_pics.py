class HangmanPics:

    def __init__(self):
        self.hangman_pics = ['''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    def get_pic(self, guess_count):
        if guess_count >= 7:
            return self.hangman_pics[0]
        elif guess_count == 6:
            return self.hangman_pics[1]
        elif guess_count == 5:
            return self.hangman_pics[2]
        elif guess_count == 4:
            return self.hangman_pics[3]
        elif guess_count == 3:
            return self.hangman_pics[4]
        elif guess_count == 2:
            return self.hangman_pics[5]
        elif guess_count == 1:
            return self.hangman_pics[6]
        elif guess_count == 0:
            return self.hangman_pics[7]

if __name__ == "__main__":
    pass