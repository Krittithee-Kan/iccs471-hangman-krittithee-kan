from collections.abc import Iterable, Mapping


def validate_difficulty(difficulty: str) -> bool:
    """Return whether the difficulty is easy, medium, or hard."""
    return isinstance(difficulty, str) and difficulty.strip().lower() in {
        "easy",
        "medium",
        "hard",
    }


def validate_lives(lives: object) -> bool:
    """Return whether lives is an integer value from 1 through 10."""
    if isinstance(lives, bool):
        return False
    if isinstance(lives, int):
        return 1 <= lives <= 10
    if not isinstance(lives, str):
        return False

    value = lives.strip()
    return value.isdecimal() and 1 <= int(value) <= 10


def filter_words_by_difficulty(
    words: Iterable[Mapping[str, str]], difficulty: str
) -> list[Mapping[str, str]]:
    """Return word entries whose word length matches the selected difficulty."""
    if not validate_difficulty(difficulty):
        raise ValueError("difficulty must be easy, medium, or hard")

    difficulty = difficulty.strip().lower()
    if difficulty == "easy":
        minimum_length, maximum_length = 3, 5
    elif difficulty == "medium":
        minimum_length, maximum_length = 6, 8
    else:
        minimum_length, maximum_length = 9, None

    matching_words = []
    for entry in words:
        word = entry["word"]
        if not isinstance(word, str):
            raise ValueError("each word entry must have a string 'word' value")
        if len(word) >= minimum_length and (
            maximum_length is None or len(word) <= maximum_length
        ):
            matching_words.append(entry)

    return matching_words


def create_game(secret_word: str, meaning: str, lives: object) -> dict[str, object]:
    """Create a game state with its fixed word, meaning, and starting lives."""
    if not isinstance(secret_word, str) or not secret_word:
        raise ValueError("secret_word must be a non-empty string")
    if not isinstance(meaning, str) or not meaning:
        raise ValueError("meaning must be a non-empty string")
    if not validate_lives(lives):
        raise ValueError("lives must be an integer from 1 through 10")

    return {
        "secret_word": secret_word,
        "meaning": meaning,
        "lives": int(lives),
    }
