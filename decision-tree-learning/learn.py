from utils import read_attributes_definition_file, read_sample_training_file
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

    # Convert continious values to discrete values
    # This is very hacky
    for attribute in order:
        if continuous[attribute]:
            sv = sorted(float(sample[attribute]) for sample in samples)
            for i, j in zip(sv[:-1], sv[1:]):
                cond = f"<{(i + j) / 2}"
                if len(values[attribute]) == 0 or values[attribute][-1] != cond:
                    values[attribute].append(cond)

            for sample in samples:
                i = float(sample[attribute])

                # TODO binary search if this needs to be sped up
                for cond in values[attribute]:
                    if i < float(cond[1:]):
                        sample[attribute] = cond
                        break
                else:
                    sample[attribute] = f">{values[attribute][-1][1:]}"

            values[attribute].append(f">{values[attribute][-1][1:]}")

    root = ID3(target, target_values, values, samples)

    with open(pckl_out_file, "wb") as picklefile:
        print(f"Dumping tree to {pckl_out_file}... ", end="", flush=True)
        pickle.dump(root, picklefile)
        print("Done!")