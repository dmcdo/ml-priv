from math import log2


def read_attributes_definition_file(fname):
    """
    Returns:
        target: Target Attribute
        target_values: ie, ["Yes", "No"]
        values: {Attribute -> [V1, V2, V3, ...]}
        order: [A1, A2, A3, ...]
        continuous: [<A1 is continuous>, <A2 is continuous>, ...]
            - Continuous values fillled in be make_discrete()
    """
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
    """
    Outputs [{A1: V, A2: V, ...}]
    """
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


def make_discrete(values, train_samples, test_samples, order, continuous):
    """
    Split continuous sample data into discrete values. See 3.7.2.
    """
    for attribute in order:
        if continuous[attribute]:
            # Extract values for given attribute out of samples.
            sv = sorted(float(sample[attribute]) for sample in train_samples)

            # Generate discrete attributes.
            for i, j in zip(sv[:-1], sv[1:]):
                cond = f"<{(i + j) / 2}"
                if len(values[attribute]) == 0 or values[attribute][-1] != cond:
                    values[attribute].append(cond)

            for sample in test_samples:
                # In-place swap of continious sample data with discrete values.
                i = float(sample[attribute])

                for cond in values[attribute]:
                    if i < float(cond[1:]):
                        sample[attribute] = cond
                        break
                else:
                    sample[attribute] = f">{values[attribute][-1][1:]}"

                # values[attribute] <- [A < x, A < y, ..., A < z, A > z]
                values[attribute].append(f">{values[attribute][-1][1:]}")


def get_count(target, target_values, samples):
    """
    Get counts of target attribute values in samples list.
    Returns dict in the form of {TV1: n1, TV2, n2, ...}
    """
    count = {v: 0 for v in target_values}
    for sample in samples:
        count[sample[target]] += 1

    return count


def get_entropy(target, target_values, samples):
    """
    Calculate the Entropy of a list of samples with respect
    to the target value.
    """
    count = get_count(target, target_values, samples)

    entropy = 0.0
    for value in target_values:
        p = count[value] / len(samples)
        entropy += -(p * log2(p)) if p != 0 else 0

    return entropy


def get_gain(target, target_values, values, samples, attribute):
    """
    Get information gain with respect to some target value
    and some attribute.
    """
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
