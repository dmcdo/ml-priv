import os.path
import sys
import pickle

if __name__ == "__main__":
    tree_pickle_fname = sys.argv[1] if len(sys.argv) > 1 else "tree.pkl"

    if not os.path.exists(tree_pickle_fname):
        print(f"{tree_pickle_fname} does not exist.")
        sys.exit(1)
    if os.path.isdir(tree_pickle_fname):
        print(f"{tree_pickle_fname} is a directory.")
        sys.exit(1)

    with open(tree_pickle_fname, "rb") as pf:
        root = pickle.load(pf)

        print("TREE")
        print("----", end="")
        root.print()

        print("RULES")
        print("-----")
        for rule in root.ruleset():
            if len(rule) == 1:
                print(rule[0])
            else:
                print(" ^ ".join(rule[:-1]), "=>", rule[-1])