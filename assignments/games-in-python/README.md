
# 📘 Assignment: Games in Python - Hangman

## 🎯 Objective

Build a playable Hangman game in Python. You will practice using loops, conditionals, strings, and user input to manage game state from start to finish.

## 📝 Tasks

### 🛠️ Build the Hangman Core Game

#### Description
Create the main game loop for Hangman. The program should select a secret word, let the player guess one letter at a time, and update the displayed word progress after each guess.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list of words.
- Display the hidden word using underscores for unknown letters (for example: `_ _ _ _`).
- Accept one letter guess per turn from the player.
- Reveal correctly guessed letters in all matching positions.
- Track guessed letters to avoid duplicate processing.


### 🛠️ Add Win/Loss Conditions and Feedback

#### Description
Add game-ending rules and player feedback so the game clearly communicates progress and results. The game should end when the player guesses the full word or uses all attempts.

#### Requirements
Completed program should:

- Start with a fixed number of incorrect guesses allowed.
- Decrease remaining attempts only for incorrect new guesses.
- End the game with a win message when the full word is guessed.
- End the game with a loss message when attempts reach zero, and reveal the secret word.
- Show remaining attempts after each turn.
