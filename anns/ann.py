from random import random
from math import e as euler
from typing import List, Optional
from copy import deepcopy

def random_weights(size: int):
    return [random() - 0.5 for _ in range(size)]

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
        """
        Initialization method.
        """
        self.inp = inp
        self.out = out
        self.learnrate = float(learnrate)
        self.momentum = float(momentum)

        self.layers = [[] for _ in range(num_hidden_layers + 1)]

        # First set of layers... Inp -> Layer1
        # Give each unit in the layer a random weight for each input unit.
        for _ in range(num_hidden_units):
            layer = random_weights(len(inp) + 1)
            self.layers[0].append(layer)

        # Middle layers... Layer(i-1) -> Layer(i)
        # Give each unit random weights for each unit in the prior layer.
        for i in range(1, num_hidden_layers):
            for _ in range(num_hidden_units):
                layer = random_weights(num_hidden_units + 1)
                self.layers[i].append(layer)

        # Output layer... Layer(FinalHidden) -> Layer(Output)
        for i in range(len(out)):
            layer = random_weights(num_hidden_units + 1)
            self.layers[-1].append(layer)


    def debug_print(self):
        """
        Print all units for each layer.
        """
        for layer in self.layers:
            print("\n".join(unit.__repr__() for unit in layer))
            print()


    def do_backpropagation(
        self,
        input_values: List[float],
        target_values: List[float],
    ) -> None:
        
        layers_outputs = []
        last_outputs = input_values
        for layer in self.layers:
            outputs = [ANN.sigmoid(ANN.net(last_outputs, unit)) for unit in layer]
            layers_outputs.append(outputs)
            last_outputs = outputs

        pass


    @staticmethod
    def net(input: List[float], unit: List[float]):
        return sum(w * x for w, x in zip(unit, [1, *input]))
    

    @staticmethod
    def sigmoid(y):
        return 1 / (1 + euler**(-y))


    @staticmethod
    def from_file(
        filename: str,
        learnrate: float,
        momentum: float,
        num_hidden_units: int,
        num_hidden_layers: int,
    ) -> "ANN":
        with open(filename, "r") as infile:
            lines = [line.strip() for line in infile]
            split_pnt = lines.index("")
            inp_lines = lines[:split_pnt]
            out_lines = lines[split_pnt + 1:]

        return ANN(
            [line.split()[1:] for line in inp_lines],
            [line.split()[1:] for line in out_lines],
            learnrate,
            momentum,
            num_hidden_units,
            num_hidden_layers,
        )