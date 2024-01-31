Instructions
------------
First, compile the code by executing:
$ make

To run the self-trainer, execute:
$ make testNoTeacher

To run the interactive teacher trainer, execute:
$ make testTeacher

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
