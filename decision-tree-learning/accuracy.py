from utils import *
import sys
import pickle


def get_accuracy(root, target, samples):
    """
    Compute the % accuracy of a tree on a sample list with
    respect to a target value.
    """
    return sum(root.answer(sample) == sample[target] for sample in samples) / len(samples)


if __name__ == "__main__":
    try:
        attr_def_file = sys.argv[1]
        attr_trn_file = sys.argv[2]
        attr_tst_file = sys.argv[3]
        pckl_in_file = sys.argv[4] if len(sys.argv) > 3 else "tree.pkl"
    except IndexError:
        print("Invalid Arguments.")
        sys.exit(1)

    target, target_values, values, order, continuous = read_attributes_definition_file(attr_def_file)
    train_samples = read_sample_training_file(attr_trn_file, target, order)
    test_samples = read_sample_training_file(attr_tst_file, target, order)
    make_discrete(values, train_samples, test_samples, order, continuous)

    with open(pckl_in_file, "rb") as picklefile:
        root = pickle.load(picklefile)

    print(f"Accuracy: {100 * get_accuracy(root, target, test_samples)}%")
    print()