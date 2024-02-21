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
        root.print()
