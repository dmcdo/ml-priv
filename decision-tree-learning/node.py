from utils import *


class Node:
    def __init__(self):
        self.attribute = None
        self.label = None
        self.ratio = None
        self.children = {}

    def answer(self, sample):
        """
        Get target value for instance.
        """
        if self.label:
            return self.label

        return self.children[sample[self.attribute]].answer(sample)

    def print(self, depth=0):
        """
        Print the tree.
        """
        if self.label:
            print(f" : {self.label} {self.ratio}", end="")
        else:
            for edge, child in self.children.items():
                print()
                print(f"|   " * depth, end="")
                print(f"{self.attribute} = {edge}", end="")
                child.print(depth + 1)
        if depth == 0:
            print()
            print()

    def ruleset(self):
        """
        Compute the rule set equivalent to the tree.
        """
        if self.label:
            return [[self.label]]
        else:
            ruleset = []
            for edge, child in self.children.items():
                for rule in child.ruleset():
                    ruleset.append([(self.attribute, edge), *rule])
            return ruleset


def ID3(target, target_values, values, samples):
    """
    The ID3 tree builder algorithm. See Table 3.1.
    """
    root = Node()

    for value in target_values:
        if all(s[target] == value for s in samples):
            root.label = value
            root.ratio = len(samples), 0
            return root
    if len(values.keys()) == 0:
        count = get_count(target, target_values, samples)
        most_common_attribute, instances = max(count.items(), key=lambda c: c[1])
        root.label = most_common_attribute
        root.ratio = instances, sum(count.values()) - instances
        return root

    max_attr = None
    max_gain = float("-inf")
    for attr in values.keys():
        gain = get_gain(target, target_values, values, samples, attr)
        if gain > max_gain:
            max_attr = attr
            max_gain = gain

    root.attribute = max_attr
    for value in values[max_attr]:
        samples_vi = [s for s in samples if s[max_attr] == value]
        if len(samples_vi) > 0:
            new_values = values.copy()
            new_values.pop(max_attr)
            root.children[value] = ID3(target, target_values, new_values, samples_vi)
        else:
            count = get_count(target, target_values, samples)
            most_common_attribute, instances = max(count.items(), key=lambda c: c[1])
            root.children[value] = Node()
            root.children[value].label = most_common_attribute
            root.children[value].ratio = instances, sum(count.values()) - instances

    return root
