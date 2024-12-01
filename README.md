# Hangman Game

This is the story about the **Hangman Game.** This is a project written with Python codes aimed at getting players to guess correctly
a randomly selected word from a pool of list containing the first twenty elements.

Link to the live project: [Hangman Game](https://hang-man-app-a6a9afadde6e.herokuapp.com/)
![Hangman Responsive image](doc/images/Hangman-Responsive-image.png)

## Content
- [How TO PLAY](#how-to-play)
- [USER EXPERIENCE](#user-experience)
- [FEATURES](#features)
- [IMPORTED LIBRARIES](#imported-libraries)
- [TECHNOLOGIES USED](#technologies-used)
- [TESTING](#testing)
- [DEPLOYMENT](#deployment)
- [CREDITS](#credits)

## HOW TO PLAY
The hangman game is a game of guessing words between the computer and a player. The computer will
select a random word from a pool of lists containing the first twenty elements and the player guesses letters to form the word selected.
The player has the chance for six(6) wrong guesses and after that will be signalled game over.
However, there is also a chance for the player to choose if he/she wants to play once more.


#### Play The Game
- When the game is started, a welcome message displays.
- Two lines of guides are also displayed to give you a clue on the kind of words you may be guessing.

#### Guessing A Word
- The hangman skeleton structure displays.
- This next line displays the word to guess.
- When you input the correct input you will be signaled CORRECT INPUT.
- The player will also be instructed to give letters in lowercase. 

#### How To Win 
- If the player guesses the correct word no full hangman will be drawn
- If the player is able to guess the word before the full hangman is drawn, he/she wins the game.

#### Game Over
- Every player has the chance to make 6 wrong guesses
- If a player cannot guess the correct letters for the selected element, the full hangman is drawn and you lose the game.

#### Replay
- After a win or a loss by a player, a message is displayed to play again or end the game.
- If you select Y, you play the game again, if you select N the game will end.

#### Additional Features
- If a player inputs one letter twice and it's not in the word like that, it will be ignored.
- If a player makes six incorrect guesses, the game is over.