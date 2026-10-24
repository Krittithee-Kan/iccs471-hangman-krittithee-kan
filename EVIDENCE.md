# Checks and decisions  

## Concrete checks
Write the first two expectations before implementation. Fill in actual results after running them.

| Check / requirement | Given | When | Expected result | Actual result / pass or fail |
|---|---|---|---|---|
| C1 / R1 — normal case | A new game with the word `apple`, 6 lives, no letters guessed | Guess `p` | The word shows `_ p p _ _` and lives are still 6 | |
| C2 / R3 — invalid guesses | A game with the word `apple`, `p` already guessed, 6 lives | Guess `p` again, then `3` | Each shows a message; the word still shows `_ p p _ _` and lives are still 6 | |

## Two review decisions
- Plan decision: [Complete after reviewing Copilot's plan.]
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
