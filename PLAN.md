# Implementation plan

## Steps
1. **Validate settings and difficulty ranges.** In `game.py`, implement `validate_difficulty()`, `validate_lives()`, and `filter_words_by_difficulty()` for supported settings and word-length ranges. Covers R1 and R3.
2. **Load words and initialize a round.** In `main.py`, implement `load_words()` with the standard-library `csv` module and select a random eligible word from `words.csv`. In `game.py`, implement `create_game()` to initialize the secret word, meaning, and lives. Covers R1.
3. **Prompt for settings and guesses.** In `main.py`, implement `choose_settings()` to prompt again when `validate_difficulty()` or `validate_lives()` returns invalid, and `play_game()` to collect player guesses and display the game. Keep all `input()` and `print()` calls in `main.py`, not `game.py`. Covers R1–R3.
4. **Implement guess handling and outcomes.** In `game.py`, implement `validate_guess()`, `guess_letter()`, `is_won()`, and `is_lost()` to handle valid, repeated, correct, and incorrect guesses, lives, and completion. In `main.py`, display the outcome and word meaning when the round ends. Covers R2 and R3.
5. **Automate evidence checks and boundaries.** In `tests/test_game.py`, automate C1 by checking that guessing `p` in `apple` reveals `_ p p _ _` without reducing 6 lives; automate C2 by checking that a repeated `p` and `3` are rejected without changing the mask or lives; and automate C3 by checking that lives `0` and `11` are rejected, `10` is accepted, and settings prompting retries. Also test difficulty boundaries exactly: 5 letters = easy, 6 = medium, 8 = medium, and 9 = hard. Run the tests with `python -m pytest`. Covers R1–R3.
6. **Try a complete two-round play-through.** Add a valid easy-length word and meaning to `words.csv`, then play an easy round and a hard round. Check that each game progresses and that the word meaning is shown at the end of both rounds. Covers R1–R3.

## Later changes, if any
None.
