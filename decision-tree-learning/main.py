from utils import read_attributes_definition_file, read_sample_training_file
from node import ID3


if __name__ == "__main__":
    # target, target_values, values, order, continuous = read_attributes_definition_file("tennis-attr.txt")
    target, target_values, values, order, continuous = read_attributes_definition_file("iris-attr.txt")
    # print(target)
    # print(target_values)
    # print(order)
    # print(values)

    # samples = read_sample_training_file("tennis-train.txt", target, order)
    samples = read_sample_training_file("iris-train.txt", target, order)

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
    root.print()