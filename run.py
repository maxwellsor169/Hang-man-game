import random
import string

MAX_INCORRECT_GUESSES = 6

def selected_word():
    with open("gaming_words.txt", mode="r") as words:
        word_list = words.readlines()
    return random.choice(word_list)

    

