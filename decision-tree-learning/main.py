from utils import read_attributes_definition_file, read_sample_training_file
from node import ID3


if __name__ == "__main__":
    target, target_values, values, order = read_attributes_definition_file("tennis-attr.txt")
    # target, target_values, values, order = read_attributes_definition_file("iris-attr.txt")
    # print(target)
    # print(target_values)
    # print(order)
    # print(values)

    samples = read_sample_training_file("tennis-train.txt", target, order)
    # samples = read_sample_training_file("iris-train.txt", target, order)
    print(samples)

    root = ID3(target, target_values, values, samples)
    root.print()