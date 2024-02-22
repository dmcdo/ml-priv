from utils import *
from node import *
from accuracy import *
import sys
from main import print_ruleset
from copy import deepcopy
import random


if __name__ == "__main__":
    try:
        attr_def_file = sys.argv[1]
        attr_trn_file = sys.argv[2]
        attr_tst_file = sys.argv[3]
    except IndexError:
        print("Invalid arguments.")
        sys.exit(1)

    corruption_percent = 0.0
    while corruption_percent <= 0.2:
        print(f"Corruption: {100 * corruption_percent}%")

        # Read in Attribute definitions, testing data, training data
        target, target_values, values, order, continuous = read_attributes_definition_file(attr_def_file)
        train_samples = read_sample_training_file(attr_trn_file, target, order)
        test_samples = read_sample_training_file(attr_tst_file, target, order)
        make_discrete(values, test_samples, train_samples, order, continuous)

        # Corrupt corruption_percent% of the samples
        corrupted_samples = random.sample(train_samples, round(corruption_percent * len(train_samples)))
        for sample in corrupted_samples:
            sample[target] = random.choice(list(set(target_values).difference({sample[target]})))

        # Build tree, rules, prune rules
        root = ID3(target, target_values, values, train_samples)
        ruleset = root.ruleset()
        pruned_ruleset = do_post_prune(ruleset, test_samples, target)

        # Accuracy
        print("Accuracy of pre-prune ruleset on training data:", get_accuracy(ruleset, train_samples, target))
        print("Accuracy of pre-prune ruleset on testing data:", get_accuracy(ruleset, test_samples, target))
        print("Accuracy of post-prune ruleset on training data:", get_accuracy(pruned_ruleset, train_samples, target))
        print("Accuracy of post-prune ruleset on testing data:", get_accuracy(pruned_ruleset, test_samples, target))
        print()

        corruption_percent += 0.02