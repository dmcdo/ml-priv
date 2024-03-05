from ann import ANN
import os
import os.path


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    ann = ANN.from_file("identity-attr.txt", 0.1, 0.1, 8, 1)
    ann.debug_print()

    ann.do_backpropagation(
        list(map(float, [1, 0, 0, 0, 0, 0, 0, 0])),
        list(map(float, [1, 0, 0, 0, 0, 0, 0, 0])),
    )