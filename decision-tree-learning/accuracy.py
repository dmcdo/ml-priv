from utils import *
import sys
import pickle


def rule_applies(rule, sample):
    """
    T/F: Does the given rule apply to the given sample?
    """
    return all(sample[attr] == value for attr, value in rule[:-1])


def get_accuracy(ruleset, samples, target):
    """
    Compute the % accuracy of a tree on a sample list with
    respect to a target value.
    """
    correct = 0

    for sample in samples:
        for rule in ruleset:
            if rule_applies(rule, sample):
                correct += int(sample[target] == rule[-1])
                break
        else:
            raise RuntimeError("This shouldn't happen.")

    return correct / len(samples)


def do_post_prune(ruleset, samples, target):
    """
    Post-pruning algorithm described in 3.7.12
    """
    new_ruleset = []
    new_accs = []

    for rule in ruleset:
        # Overall accuracy
        applicable_samples = [s for s in samples if rule_applies(rule, s)]
        if len(applicable_samples) == 0:
            new_ruleset.append(rule)
            new_accs.append(1.0)
            continue

        accuracy = get_accuracy([rule], applicable_samples, target)
        if accuracy < 1:
            pass  # Debug

        # If removing a condition increases accuracy, we will prune it soon.
        conditions_to_prune = set()
        for i in range(len(rule)):
            pruned = rule[0:i] + rule[i + 1:]
            pacc = get_accuracy([pruned], applicable_samples, target)
            if pacc > accuracy:
                conditions_to_prune.add(i)

        # Prune bad conditions
        new_rule = [rule[i] for i in range(len(rule)) if i not in conditions_to_prune]
        new_acc = get_accuracy([new_rule], applicable_samples, target)
        new_ruleset.append(new_rule)
        new_accs.append(new_acc)

    return [rule for rule, _ in sorted(zip(new_ruleset, new_accs), key=lambda x: x[1])]
