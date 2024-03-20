from ann import ANN
import os
import os.path
import argparse
import copy

from typing import List, Optional


def main(argv: Optional[List[str]] = None):
    # Parse variable arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data-set", type=str, default="identity")
    parser.add_argument("-n", "--num-hidden-units", type=int, default=3)
    parser.add_argument("-l", "--learn-rate", type=float, default=0.3)
    parser.add_argument("-m", "--momentum", type=float, default=0.3)
    parser.add_argument("-e", "--epochs", type=int, default=5000)
    parser.add_argument("--show-propagation", action="store_true")
    arguments = parser.parse_args(argv)

    # Initialize the ANN
    ann = ANN.from_file(
        filename=f"{arguments.data_set}-attr.txt",
        num_hidden_units=arguments.num_hidden_units,
        learnrate=arguments.learn_rate,
        momentum=arguments.momentum,
    )

    # Read training, test data.
    samples = ANN.training_samples_from_file(f"{arguments.data_set}-train.txt")

    if os.path.exists(f"{arguments.data_set}-train-uncorrupted.txt"):
        uncorrupted_samples = ANN.training_samples_from_file(f"{arguments.data_set}-train-uncorrupted.txt")
    else:
        uncorrupted_samples = None

    if os.path.exists(f"{arguments.data_set}-test.txt"):
        test_samples = ANN.training_samples_from_file(f"{arguments.data_set}-test.txt")
    else:
        test_samples = None

    # Do training
    for _ in range(arguments.epochs):
        for sample in samples:
            ann.do_backpropagation(*sample)

    # Print results
    amt_got_correct = 0
    for sample in samples:
        prop = ann.propagate(sample[0])
        result = prop[-1]
        result = ann.decode_output_values(result)
        amt_got_correct += int(result == sample[1])

        if arguments.show_propagation:
            hidden_results, output_results = prop
            hidden_reprs = [str(round(100 * r) / 100) for r in hidden_results]
            output_reprs = [str(round(100 * r) / 100) for r in output_results]
            print(f"{' '.join(sample[0])} -> {' '.join(hidden_reprs)} -> {' '.join(output_reprs)}")

    if uncorrupted_samples:
        print(f"Corrupted training data: {round(100 * amt_got_correct / len(samples))}% correct.")
        print("----------------")
    else:
        print(f"Training data: {round(100 * amt_got_correct / len(samples))}% correct.")
        print("----------------")


    if uncorrupted_samples is not None:
        amt_got_correct = 0
        for sample in uncorrupted_samples:
            prop = ann.propagate(sample[0])
            result = prop[-1]
            result = ann.decode_output_values(result)
            amt_got_correct += int(result == sample[1])

        print(f"Uncorrupted training data: {round(100 * amt_got_correct / len(samples))}% correct.")
        print("----------------")

    if test_samples is not None:
        amt_got_correct = 0
        for sample in test_samples:
            prop = ann.propagate(sample[0])
            result = prop[-1]
            result = ann.decode_output_values(result)
            amt_got_correct += int(result == sample[1])

            if arguments.show_propagation:
                hidden_results, output_results = prop
                hidden_reprs = [str(round(100 * r) / 100) for r in hidden_results]
                output_reprs = [str(round(100 * r) / 100) for r in output_results]
                print(f"{' '.join(sample[0])} -> {' '.join(hidden_reprs)} -> {' '.join(output_reprs)}")

        print(f"Test data: {round(100 * amt_got_correct / len(samples))}% correct.")
    else:
        print("No test data set available.")


if __name__ == "__main__":
    main()