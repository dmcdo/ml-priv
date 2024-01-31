Instructions
------------
First, compile the code by executing:
$ make

To run the self-trainer, execute:
$ make testNoTeacher

To run the teacher trainer, execute:
$ make testTeacher

    This default game file is "games.txt". You may provide your own game
    file by running "make testTeacher GAMEFILE=customgame.txt".

    The game file is of the following format:
        - N       (N games wil follow)
        - P       (Starting player, X or O)
        - x y     (x and y position of the next player's move)
        - x y
        - ...
        - -1 -1   (Signifies the end of a game)
        - P
        - x y
        - x y
        - ...

    Training examples that do not end in finished games will be ignored.

To run the interactive teacher trainer, execute:
$ make testTeacherInteractive

To reset the weights, execute:
$ make reset

The weights represent the following metrics:
    w0 - w0
    w1 - Number of opportunities X has to win in 2 moves.
    w2 - Number of opportunities X has to win in 1 move.
    w3 - Number of opportunities X has to win in 0 moves. (ie, X has won.)
    w4 - Number of opportunities O has to win in 2 moves.
    w5 - Number of opportunities O has to win in 1 moves.
    w6 - Unused. Always 0. Ignored by training algorithm.
    w7 - Unused. Always 0. Ignored by training algorithm.
