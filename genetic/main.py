import argparse
import os
import typing
from pathlib import Path

from attr import AttributeDefinition
from individual import Individual


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

    for _ in range(arguments.population):
        indiv = Individual.from_attr(attr)
        print(indiv)



if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    main()