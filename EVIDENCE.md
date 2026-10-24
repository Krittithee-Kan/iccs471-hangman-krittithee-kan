# Checks and decisions  

## Concrete checks
Write the first two expectations before implementation. Fill in actual results after running them.

| Check / requirement | Given | When | Expected result | Actual result / pass or fail |
|---|---|---|---|---|
| C1 / R2 — normal case | A new game with the word `apple`, 6 lives, no letters guessed | Guess `p` | The word shows `_ p p _ _` and lives are still 6 | Pass — the word showed `_ p p _ _` and lives stayed 6 (`test_c1...`) |
| C2 / R3 — invalid guesses | A game with the word `apple`, `p` already guessed, 6 lives | Guess `p` again, then `3` | Each shows a message; the word still shows `_ p p _ _` and lives are still 6 | Pass — both printed "Invalid guess."; the word stayed `_ p p _ _` and lives stayed 6 (both C2 tests) |
| C3 / R1, R3 — lives boundary | The lives question before a round | Enter `0`, then `11`, then `10` | `0` and `11` show a message and ask again; `10` is accepted and the round starts with 10 lives | Pass — `0` and `11` each printed "Invalid lives." and asked again; `10` was accepted (`test_c3...`) |

## Two review decisions
- Plan decision: Copilot's first plan put the difficulty and lives rules inside `choose_settings()` in `main.py`. I moved them to `validate_difficulty()` and `validate_lives()` in `game.py`, because `main.py` uses `input()` and is hard to test, and C3 needs an automated check that 0 and 11 lives are rejected. I also replaced its play-through, which had me guess a word I could already see, with two real rounds that include a word I added.
- Code decision: [Complete during implementation.]

## Automated tests
- Test file and behaviour checked:  `tests/test_game.py` — C1 letter reveal, C2 invalid and repeated guesses cost no life, C3 lives 0/11 rejected and 10 accepted, R2 losing shows the word and its meaning, and difficulty boundaries (5 letters = easy, 6 and 8 = medium, 9 = hard).
- Command I ran: `python -m pytest`
- Final result: 9 passed
- Correction and rerun, if needed: Copilot's first C2 test only checked the board after the whole game had finished, so I added a direct check that the board is still `_ p p _ _` right after the invalid guesses. I also made the boundary test check that each word is excluded from the other difficulties, and added an R2 test for the lose message and meaning. Reran: 9 passed.

## Realistic use and final judgment
- Task I tried: Added `rabbit,a small animal with long ears` to `words.csv`. I had Claude Code play-test two rounds as a player without looking at the word list (easy with 6 lives, hard with 4 lives, including invalid guesses), and I played [one easy round] myself with `python main.py`.
- Outcome: The game was easy to play, and wrong or repeated guesses cost no life. I won my round, and the tester lost the hard round. Showing the meaning at the end helped with vocabulary, but hard mode with 4 lives felt mostly like luck.
- Judgment: Done. R1–R3 behave as specified (all checks pass, 9 tests pass) and both play-throughs were completed from start to finish. The weaknesses found are usability issues, not requirement failures.
- Remaining limitation or unfinished work: The game doesn't show letters already guessed, so on long words players repeat letters by mistake, and the single "Invalid guess" message doesn't say whether the problem was a repeat or a non-letter. Hard mode with few lives is mostly luck, and each run plays only one round. A useful next step would be showing wrong guesses on screen.