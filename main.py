import csv
import random
from pathlib import Path

from game import (
    GameState,
    create_game,
    display_word,
    filter_words_by_difficulty,
    guess_letter,
    is_lost,
    is_won,
    validate_difficulty,
    validate_lives,
)


def load_words(path: str | Path | None = None) -> list[dict[str, str]]:
    """Load word and meaning entries from the project's CSV file."""
    words_path = Path(path) if path is not None else Path(__file__).with_name("words.csv")

    with words_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None or not {"word", "meaning"}.issubset(
            reader.fieldnames
        ):
            raise ValueError("words.csv must have 'word' and 'meaning' columns")

        words = []
        for row_number, row in enumerate(reader, start=2):
            word = (row["word"] or "").strip().lower()
            meaning = (row["meaning"] or "").strip()
            if not word or not meaning:
                raise ValueError(f"word and meaning are required on CSV row {row_number}")
            words.append({"word": word, "meaning": meaning})

    return words


def choose_random_word(
    words: list[dict[str, str]], difficulty: str
) -> dict[str, str]:
    """Choose a random word entry that matches the selected difficulty."""
    eligible_words = filter_words_by_difficulty(words, difficulty)
    if not eligible_words:
        raise ValueError(f"no words available for {difficulty} difficulty")
    return random.choice(eligible_words)


def choose_settings() -> tuple[str, int]:
    """Prompt until the player enters a supported difficulty and lives value."""
    while True:
        difficulty = input("Choose difficulty (easy/medium/hard): ").strip().lower()
        if validate_difficulty(difficulty):
            break
        print("Invalid difficulty. Choose easy, medium, or hard.")

    while True:
        lives = input("Choose lives (1-10): ").strip()
        if validate_lives(lives):
            return difficulty, int(lives)
        print("Invalid lives. Enter a number from 1 to 10.")


def play_game(game: GameState) -> None:
    """Run one round, displaying guesses, lives, and the final meaning."""
    while not is_won(game) and not is_lost(game):
        print(f"\nWord: {display_word(game)}")
        print(f"Lives: {game['lives']}")
        result = guess_letter(game, input("Guess one letter A-Z: "))

        if result == "invalid":
            print("Invalid guess. Enter one letter A-Z that you have not guessed.")
        elif result == "correct":
            print("Correct!")
        else:
            print("Wrong! You lose 1 life.")

    if is_won(game):
        print("You win!")
    else:
        print(f"You lose! The word was {game['secret_word']}")
    print(f"Meaning: {game['meaning']}")


def main() -> None:
    difficulty, lives = choose_settings()
    word_entry = choose_random_word(load_words(), difficulty)
    play_game(create_game(word_entry["word"], word_entry["meaning"], lives))


if __name__ == "__main__":
    main()
