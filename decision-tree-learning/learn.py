from utils import *
from node import ID3
import sys
import pickle


if __name__ == "__main__":
    try:
        attr_def_file = sys.argv[1]
        attr_spl_file = sys.argv[2]
        pckl_out_file = sys.argv[3] if len(sys.argv) > 3 else "tree.pkl"
    except IndexError:
        print("Invalid arguments. Must be: `learn.py example-attr.txt example-train.txt`")
        sys.exit(1)

    target, target_values, values, order, continuous = read_attributes_definition_file(attr_def_file)
    samples = read_sample_training_file(attr_spl_file, target, order)
    make_discrete(values, samples, samples, order, continuous)

    root = ID3(target, target_values, values, samples)

    with open(pckl_out_file, "wb") as picklefile:
        print(f"Dumping tree to {pckl_out_file}... ", end="", flush=True)
        pickle.dump(root, picklefile)
        print("Done!")
        print()