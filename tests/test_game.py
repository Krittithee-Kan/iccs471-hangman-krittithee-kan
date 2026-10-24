import pytest

from game import (
    create_game,
    display_word,
    filter_words_by_difficulty,
    guess_letter,
    validate_lives,
)
from main import choose_settings, play_game


def test_c1_correct_guess_reveals_letters_without_losing_life() -> None:
    game = create_game("apple", "a fruit", 6)

    assert guess_letter(game, "p") == "correct"
    assert display_word(game) == "_ p p _ _"
    assert game["lives"] == 6


def test_c2_repeated_and_nonletter_guesses_are_invalid_without_life_loss() -> None:
    game = create_game("apple", "a fruit", 6)

    assert guess_letter(game, "p") == "correct"
    assert guess_letter(game, "p") == "invalid"
    assert guess_letter(game, "3") == "invalid"
    assert display_word(game) == "_ p p _ _"
    assert game["lives"] == 6


def test_c2_invalid_and_repeated_guesses_show_message_without_life_loss(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    game = create_game("apple", "a fruit", 6)
    game["guessed_letters"].add("p")
    guesses = iter(["p", "3", "a", "l", "e"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(guesses))

    play_game(game)

    output = capsys.readouterr().out
    assert output.count("Invalid guess.") == 2
    assert game["lives"] == 6
    assert display_word(game) == "a p p l e"


def test_c3_invalid_lives_are_reprompted_until_ten_is_accepted(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    inputs = iter(["easy", "0", "11", "10"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(inputs))

    assert not validate_lives("0")
    assert not validate_lives("11")
    assert validate_lives("10")
    assert choose_settings() == ("easy", 10)
    assert capsys.readouterr().out.count("Invalid lives.") == 2


@pytest.mark.parametrize(
    ("word", "difficulty"),
    [
        ("abcde", "easy"),
        ("abcdef", "medium"),
        ("abcdefgh", "medium"),
        ("abcdefghi", "hard"),
    ],
)
def test_difficulty_length_boundaries(word: str, difficulty: str) -> None:
    entries = [{"word": word, "meaning": "fixed test word"}]
    other_difficulties = {"easy", "medium", "hard"} - {difficulty}

    assert filter_words_by_difficulty(entries, difficulty) == entries
    for other_difficulty in other_difficulties:
        assert filter_words_by_difficulty(entries, other_difficulty) == []


def test_r2_losing_displays_word_and_meaning(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    game = create_game("cat", "a small domesticated animal", 1)
    monkeypatch.setattr("builtins.input", lambda _prompt="": "z")

    play_game(game)

    output = capsys.readouterr().out
    assert "You lose! The word was cat" in output
    assert "Meaning: a small domesticated animal" in output
