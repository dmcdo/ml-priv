from math import log2


def read_attributes_definition_file(fname):
    order = []
    continuous = {}
    values = {}

    with open(fname, "r") as deffile:
        while True:
            line = deffile.readline().strip()
            if line == "":
                break

            attribute, *vals = line.split()
            if vals == ["continuous"]:
                order.append(attribute)
                values[attribute] = []
                continuous[attribute] = True
            else:
                order.append(attribute)
                values[attribute] = vals
                continuous[attribute] = False

        target, *target_values = deffile.readline().strip().split()
        return target, target_values, values, order, continuous


def read_sample_training_file(fname, target, order):
    samples = []

    with open(fname, "r") as trainfile:
        for line in trainfile.readlines():
            line = line.strip()
            if line == "":
                continue

            samples.append({
                attribute: value
                for attribute, value in zip([*order, target], line.split())
            })

    return samples


def get_count(target, target_values, samples):
    count = {v: 0 for v in target_values}
    for sample in samples:
        count[sample[target]] += 1

    return count


def get_entropy(target, target_values, samples):
    count = get_count(target, target_values, samples)

    entropy = 0.0
    for value in target_values:
        p = count[value] / len(samples)
        entropy += -(p * log2(p)) if p != 0 else 0

    return entropy


def get_gain(target, target_values, values, samples, attribute):
    entropy = get_entropy(target, target_values, samples)

    S = {v: [] for v in values[attribute]}
    for sample in samples:
        S[sample[attribute]].append(sample)

    summation = 0.0
    for value in values[attribute]:
        if len(S[value]) == 0:
            continue

        summation += (len(S[value]) / len(sample)) * get_entropy(target, target_values, S[value])

    return entropy - summation
