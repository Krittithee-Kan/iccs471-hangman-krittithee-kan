## Purpose
This is a small Hangman game on computer. It is for people who want to practice English word. Player will guess the word by letter. After that, they will know the meaning of the word.

## Requirements
- R1: Before the game start, player must choose difficulty. Easy is 3-5 letters, medium is 6-8 letters, and hard is 9 letters or more. Player also choose life from 1 to 10. Then, the game will pick random word from words.csv. Player can add their word and meaning in this file too.
- R2: The game will show the word like _ _ _ _ _. If you guess correct letter, it will show the letter in the word. If you guess wrong letter, you will lose 1 life. The game will finish and say "You win!" if you find all letter. If your life is 0, it will say "You lose! The word was X". For both way, the game will tell you the meaning of the word.
- R3: When you guess, you must type only one letter A-Z (big or small is ok). If you type nothing, or not a letter, or more than one letter, or letter you already guessed, the game will show message and you do not lose life. If you type difficulty that is not easy/medium/hard, or life not 1-10, the game will show message and ask you to type again.

## Setup and use
- Prerequisites: Python 3.10+, pytest (for tests only).
- Setup: [Fill in once chosen, e.g. `pip install pytest`.]
- Run: [Fill in once built, e.g. `python main.py`, then a short example.]
- Add your own word: open `words.csv` and add a line in the form `word,meaning`, e.g. `rabbit,a small animal with long ears`. Its difficulty is set by its length.
- Run tests: [Fill in once chosen, e.g. `python -m pytest`.]

## Author and acknowledgements
- Name / student ID: Krittithee Kanjanapinchote 6580988
- AI tools used: GitHub Copilot
- External code/resources: None

See PLAN.md for the implementation plan and EVIDENCE.md for results and decisions.