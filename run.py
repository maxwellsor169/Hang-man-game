"""The main Hang man game file."""
import random
from colorama import Fore, init

init()

MAX_INCORRECT_GUESSES = 6


def selected_word():
    """Choose the word to be selected by the computer."""
    with open("gaming_words.txt", mode="r") as words:
        word_list = words.readlines()
    return random.choice(word_list).strip()


def get_player_input(guessed_letters):
    """Get the guessing player's input."""
    while True:
        print("Your guessed letters should be in small cases")
        player_input = input("Guess a letter:\n").lower()

        if _validate_input(player_input, guessed_letters):
            print("Correct input")
            break
    return player_input


def _validate_input(player_input, guessed_letters):
    """Validate the guessing player's inputs."""
    try:
        if len(player_input) != 1:
            raise ValueError(
                f"Write one letter, you wrote {len(player_input)}")
    except ValueError as e:
        print(
            Fore.RED +
            f"{player_input} is not in guessed_letters: {e}"
            + Fore.RESET)
        return False
    return True


def join_guessed_letters(guessed_letters):
    """Join the guessed letters to produce the selected word."""
    return " ".join(sorted(guessed_letters))


def build_guessed_word(target_word, guessed_letters):
    """Build all the guessed letters together."""
    current_letters = []
    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("_")
    return " ".join(current_letters)


def draw_hanged_man(wrong_guesses):
    """Draws the hanged man whenever a wrong guess is made."""
    hanged_man = [
        r"""
   -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[wrong_guesses])


def game_over(wrong_guesses, target_word, guessed_letters):
    """Check if your number of wrong guesses."""
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        return True
    if set(target_word) <= guessed_letters:
        return True
    return False


def game_loop():
    """Declare all the initial conditions for the game loop to run."""
    target_word = selected_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0
    print(Fore.GREEN + "WELCOME TO HANGMAN GAME" + Fore.RESET)
    print("Your guessed words will be selected from the first twenty elements")
    print("Example: hydrogen, boron")
    # This while loop will run the Game in a loop
    while not game_over(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man(wrong_guesses)
        print(f"Your word is: {guessed_word}")
        print(
            "Current guessed letters: "
            f"{join_guessed_letters(guessed_letters)}\n"
        )
        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            print("Great guess!")
        else:
            print("Sorry, it's not there.")
            wrong_guesses += 1

        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)
    # The following conditions will run the Game over function
    draw_hanged_man(wrong_guesses)
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        print("Sorry, you lost!")
    else:
        print("Congrats! You did it!")
    print(f"Your word was: {target_word}")


if __name__ == "__main__":
    game_loop()


def replay():
    """Play or end the game again if you want."""
    while True:
        try:
            print("Would you like to play again?\n")
            restart_game = input("Y or N:\n").upper()
            if restart_game == "Y":
                print("Lets play again")
                game_loop()
                break
            elif restart_game == "N":
                print("Thank you for playing!\n")
                break
            else:
                print("Please Enter: Y or N\n")
        except ValueError:
            print("Please Enter: Y or N\n")


def main():
    """Replay the game again."""
    replay()


if __name__ == "__main__":
    main()
