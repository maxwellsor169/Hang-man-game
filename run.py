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

def _validate_input(palyer_input, guessed_letters):
    """
    This function will check the validation of the guessing player's inputs
    """
    try:
        if len(player_input) != 1:
            raise ValueError(
                f"You have to give only one letter, you gave {len(player_input)}"
            )
    except ValueError as e:
            print(Fore.RED + f"{player_input} is not in guessed_letters: {e}")
            return False

    return True

def join_guessed_letters(guessed_letters):
    """
    This function will join the guessed letters to produce the selected word
    """
    return " ".join(sorted(guessed_letters))           
