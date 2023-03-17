# Connect 4

## Requirements

1. Saves to file
2. Reads from file
3. At least 1 struct
4. At least 1 array
5. Pointers and pointer arithmetic
6. 15 points (see below)

## Features 

1. 2 players, player vs AI, and AI vs AI
2. Connect 4 instead of rock-paper-scissors
3. The game always has a save of the current game
    - If the program is run, it will try to load an unfinished game
    - If there is no save file, or the game was finished, a new game is created
6. 1 struct: Board
7. (9) Multiple enums: Spot and ControlOptions
11. Board is passed (as a pointer) to many functions
    - Board is returned as part of a tuple from readSaveGameData()
12. (13) Multiple arrays. Examples:
    - Game state is saved as a 2d array of Spot
    - Not filled columns (valid/open moves) saved as an array of bool
    - vector used in minimax to make the code easier to read
        - (Not used everywhere for excuses to use pointer arithmetic)
14. (16) Pointer arithmetic used twice when iterating over Board->nonFilledColumn
17. Board is passed as a pointer everywhere to avoid copying
    - And to allow editing/updating/changing it without also returning it
19. (+5 points) 2 levels of AI
    - Easy: randomly chooses a column
    - Hard: soft-fail minimaX
        - If it does not find the end of a game, it prioritizes moves in the middle
        - Not unbeatable (doesn't always look to the end of a game), but very hard to beat
    - We feel that this feature more than makes up for all the bad and inconsistent code