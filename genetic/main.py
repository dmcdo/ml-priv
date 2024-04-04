import argparse
import os
import typing
from pathlib import Path

from attr import AttributeDefinition
from hypothesis import Rule, Hypothesis
from ga import fitness, GA
from sample import SampleSet


def main(argv: typing.Optional[typing.List[str]] = None) -> None:
    # Parse variable arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data-set", type=str, default="tennis")
    parser.add_argument("-p", "--population", type=int, default=10)
    # parser.add_argument("-r", "--replacement-rate", type=int, default=1)
    # parser.add_argument("-m", "--mutation-rate", type=int, default=1)
    # TODO stopping criterion
    # TODO selection strategy
    arguments = parser.parse_args(argv)

    attr = AttributeDefinition(arguments.data_set)
    test_samples = SampleSet(arguments.data_set, "test")
    train_samples = SampleSet(arguments.data_set, "train")

    for _ in range(arguments.population):
        hypothesis = Hypothesis.random_from_attr(attr)
        # print(hypothesis)
        print(fitness(hypothesis, test_samples))
        print(fitness(hypothesis, train_samples))
        print()



if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    main()