# Checks and decisions  

## Concrete checks
Write the first two expectations before implementation. Fill in actual results after running them.

| Check / requirement | Given | When | Expected result | Actual result / pass or fail |
|---|---|---|---|---|
| C1 / R1 — normal case | A new game with the word `apple`, 6 lives, no letters guessed | Guess `p` | The word shows `_ p p _ _` and lives are still 6 | |
| C2 / R3 — invalid guesses | A game with the word `apple`, `p` already guessed, 6 lives | Guess `p` again, then `3` | Each shows a message; the word still shows `_ p p _ _` and lives are still 6 | |
| C3 / R1, R3 — lives boundary | The lives question before a round | Enter `0`, then `11`, then `10` | `0` and `11` show a message and ask again; `10` is accepted and the round starts with 10 lives | |

## Two review decisions
- Plan decision: Copilot's first plan put the difficulty and lives rules inside `choose_settings()` in `main.py`. I moved them to `validate_difficulty()` and `validate_lives()` in `game.py`, because `main.py` uses `input()` and is hard to test, and C3 needs an automated check that 0 and 11 lives are rejected. I also replaced its play-through, which had me guess a word I could already see, with two real rounds that include a word I added.
- Code decision: [Complete during implementation.]

## Automated tests
- Test file and behaviour checked: [...]
- Command I ran: [...]
- Final result: [...]
- Correction and rerun, if needed: [...]

## Realistic use and final judgment
- Task I tried: [...]
- Outcome: [...]
- Judgment: [...]
- Remaining limitation or unfinished work: [...]