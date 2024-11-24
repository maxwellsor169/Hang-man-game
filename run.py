import random
import string
from colorama import Fore, init

init()

MAX_INCORRECT_GUESSES = 6




def selected_word():
    """
    This function will target the word to be selected by the computer
    """
    with open("gaming_words.txt", mode="r") as words:
       word_list = words.readlines()
    return random.choice(word_list)

def get_player_input(guessed_letters):
    """
    Get the guessing player's input
    """

    while True:
        print("Your guessed letters should be in small cases")
        player_input = input("Guess a letter:\n").lower()

        if _validate_input(player_input, guessed_letters):
            return player_input        
