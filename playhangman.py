import string
import random
from wordlist import words
import curses

word = random.choice(words)

class Game():

    def __init__(self, word):
        self.attempts = 0
        self.word = words
        self.game_progress = list('_' * len(self.word))

        
    word = random.choice(words)
    def play_hangman(self):
        word = random.choice(words)
        correct_letters = set(word)
        letters = set(string.ascii_lowercase)
        guessed_letters = set()
        attempts = 6
        while len(correct_letters) > 0 and attempts > 0:
            print("You currently have ", attempts, "attempts left. You have used these letters so far: ", " ".join(guessed_letters))

            word_list = [letter if letter in guessed_letters else "_" for letter in word]
            print("Current Word: ", " ".join(word_list))

            letter_input = input("Try guessing a letter! ").lower()
            if letter_input in letters - guessed_letters:
                guessed_letters.add(letter_input)
                if letter_input in correct_letters:
                    correct_letters.remove(letter_input)
                else:
                    attempts -= 1
                    print("Sorry! This letter is not in the word.")

            elif letter_input in guessed_letters:
                print("This Letter has already been guessed. Please choose another letter!")

            else: 
                print("This is not a valid guess. Please enter a letter!")

        if attempts == 0:
            print("GAME OVER! The correct word was", word, "!")
            while True:
                try:
                    choice = input("Want to play again? (Y/N:")
                    if choice.upper() == "Y":
                        word = random.choice(words)
                        hangman.play_hangman()
                    #How can I implement the No option?
                    else:
                        exit() 
                except Exception:
                    print("Exit Game")
        else:
            print("Woohoo! You correctly guessed the word", word, "!")
            exit()


if __name__ == "__main__":
    word = random.choice(words)
    hangman = Game(word)
    hangman.play_hangman()