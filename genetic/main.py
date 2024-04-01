import argparse

import typing

from attr import AttributeDefinition



def main(argv: typing.Optional[typing.List[str]] = None) -> None:
    # Parse variable arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data-set", type=str, default="tennis")
    # parser.add_argument("-p", "--population-size", type=int, default=1)
    # parser.add_argument("-r", "--replacement-rate", type=int, default=1)
    # parser.add_argument("-m", "--mutation-rate", type=int, default=1)
    # TODO stopping criterion
    # TODO selection strategy
    arguments = parser.parse_args(argv)

    attr = AttributeDefinition(arguments.data_set)
    print(attr)




if __name__ == "__main__":
    main()