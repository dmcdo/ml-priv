from utils import *
from node import *
from accuracy import *
import sys


def print_ruleset(ruleset):
    def format_condition(condition):
        if condition[1][0] in "><":
            left = condition[0]
            operator = condition[1][0]
            right = condition[1][1:]
        else:
            left = condition[0]
            operator = "="
            right = condition[1]
        return f"{left} {operator} {right}"

    for rule in ruleset:
        conclusion = rule[-1]
        conditions = rule[:-1]
        if len(conditions) == 0:
            print(conclusion)
        else:
            print(" ^ ".join(format_condition(c) for c in conditions), "=>", conclusion)


def main():
    try:
        attr_def_file = sys.argv[1]
        attr_trn_file = sys.argv[2]
        attr_tst_file = sys.argv[3]
    except IndexError:
        print("Invalid arguments.")
        sys.exit(1)

    # Read in Attribute definitions, testing data, training data
    target, target_values, values, order, continuous = read_attributes_definition_file(attr_def_file)
    train_samples = read_sample_training_file(attr_trn_file, target, order)
    test_samples = read_sample_training_file(attr_tst_file, target, order)
    make_discrete(values, test_samples, train_samples, order, continuous)

    # Create decision tree via ID3
    root = ID3(target, target_values, values, train_samples)
    print("Printing the tree:", end="", flush=True)
    root.print()

    # Generate ruleset from tree
    ruleset = root.ruleset()
    print("Printing the pre-pruned ruleset:")
    print_ruleset(ruleset)
    print()

    # Perform post-pruning
    pruned_ruleset = do_post_prune(ruleset, test_samples, target)
    print("Printing the post-pruned ruleset:")
    print_ruleset(pruned_ruleset)
    print()

    # Accuracy
    print("Accuracy of pre-prune ruleset on training data:", get_accuracy(ruleset, train_samples, target))
    print("Accuracy of pre-prune ruleset on testing data:", get_accuracy(ruleset, test_samples, target))
    print("Accuracy of post-prune ruleset on training data:", get_accuracy(pruned_ruleset, train_samples, target))
    print("Accuracy of post-prune ruleset on testing data:", get_accuracy(pruned_ruleset, test_samples, target))


if __name__ == "__main__":
    main()