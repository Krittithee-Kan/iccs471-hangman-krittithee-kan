import csv
import random
from pathlib import Path

from game import filter_words_by_difficulty


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
