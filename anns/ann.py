from random import random
from typing import List

class ANN:
    def __init__(
        self,
        inp: List[List[str]],
        out: List[List[str]],
        learnrate: float,
        momentum: float,
        num_hidden_units: int,
        num_hidden_layers: int,
    ):
        self.inp = inp
        self.out = out
        self.learnrate = float(learnrate)
        self.momentum = float(momentum)

        self.edges = [[] for _ in range(num_hidden_layers)]

        # First set of edges... Inp -> Layer1
        # Give each unit in the layer a random weight for each input unit.
        for _ in range(num_hidden_units):
            layer = [random() - 0.5 for _ in range(len(inp))]
            self.edges[0].append(layer)

        # Middle layers... Layer(n-1) -> Layer(n)
        # Give each unit random weights for each unit in the prior layer.
        for i in range(1, num_hidden_layers):
            for _ in range(num_hidden_units):
                layer = [random() - 0.5 for _ in range(num_hidden_units)]
                self.edges[i].append(layer)


def ann_from_file(filename: str):
    with open(filename, "r") as infile:
        lines = [line.strip() for line in infile]
        split_pnt = lines.index("")
        inp_lines = lines[:split_pnt]
        out_lines = lines[split_pnt + 1:]

    return ANN(
        [line.split()[1:] for line in inp_lines],
        [line.split()[1:] for line in out_lines],
        0,
        0,
        10,
        1,
    )