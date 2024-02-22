2. Programming assignment: Decision Tree

Description of contents:
    *-attr.txt:
    *-test.txt:
    *-train.txt:
        The attribute definitions, training data, and testing data
        provided on the course website.

    utils.py:
        Most mathematical functions in chapter 3 (ie, Gain, SplitInformation, etc.)
        as well some helper functions for the main program.
    node.py:
        Class definition of a tree node. Also defines the ID3 algorithm.
    accuracy.py:
        Functions for measuring tree accuracy and for ruleset pruning.
    main.py:
        Performs the following operating in sequence on (tennis, iris, or bool, depending on arguments)
        - Parse problem statement (ie, attr, train, test) (2a) (2e) (2f)
        - Convert continious attributes to discrete attributes (2b)
        - Generate the decision tree using ID3 (A)
        - Print the decision tree (2c) (C)
        - Generate a ruleset from the decision tree (2d)
        - Prune the ruleset (D)
        - Meaure accuracy of the original ruleset (B)
        - Measure accuracy of the pruned ruleset (B)
    corrupted-main.py:
        Modified main.py. Does testIrisNoisy.

(gi)
    $ make testTennis

(gii)
    $ make testIris

(optional)
    $ make testBool

(giii)
    $ make testIrisNoisy