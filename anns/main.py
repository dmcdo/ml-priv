from ann import ANN
import os
import os.path
import argparse

from typing import List, Optional


def main(argv: Optional[List[str]] = None):
    # Parse variable arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-set", type=str, default="identity")
    parser.add_argument("-n", "--num-hidden-units", type=int, default=8)
    parser.add_argument("-l", "--num-hidden-layers", type=int, default=1)
    parser.add_argument("-r", "--learn-rate", type=float, default=0.1)
    parser.add_argument("-m", "--momentum", type=float, default=0.1)
    arguments = parser.parse_args(argv)

    # Make sure we are running in the root project folder
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # Initialize the ANN
    ann = ANN.from_file(
        filename=f"{arguments.data_set}-attr.txt",
        num_hidden_units=arguments.num_hidden_units,
        num_hidden_layers=arguments.num_hidden_layers,
        learnrate=arguments.learn_rate,
        momentum=arguments.momentum,
    )

    ann.do_backpropagation(
        list(map(float, [1, 0, 0, 0, 0, 0, 0, 0])),
        list(map(float, [1, 0, 0, 0, 0, 0, 0, 0])),
    )


if __name__ == "__main__":
    main()