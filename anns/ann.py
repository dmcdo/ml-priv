from random import random
from math import e as euler
from typing import List, Optional, Tuple
from copy import deepcopy
from itertools import chain

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

        self.hidden_layer = [random_weights(len(inp) + 1) for _ in range(num_hidden_units)]
        self.output_layer = [random_weights(num_hidden_units + 1) for _ in range(len(out))]

    def debug_print(self):
        """
        Print all units for each layer.
        """
        print(self.hidden_layer)
        print(self.output_layer)


    def propagate(self, input_values: List[float]) -> List[List[float]]:
        layers_outputs = []
        last_outputs = input_values
        for layer in [self.hidden_layer, self.output_layer]:
            outputs = [ANN.sigmoid(ANN.net(last_outputs, unit)) for unit in layer]
            layers_outputs.append(outputs)
            last_outputs = outputs

        return layers_outputs


    def do_backpropagation(
        self,
        input_values: List[float],
        target_values: List[float],
    ) -> None:
        hidden_results, output_results = self.propagate(input_values)

        # Calculate error for output units
        output_errors = []
        for k in range(len(self.output_layer)):
            ok = output_results[k]
            tk = target_values[k]
            output_errors.append(ok * (1 - ok) * (tk - ok))

        # Calculate errors for hidden units
        hidden_errors = []
        for h in range(len(self.hidden_layer)):
            oh = hidden_results[h]
            sm = sum(self.output_layer[k][h + 1] * eterm for k, eterm in enumerate(output_errors))
            hidden_errors.append(oh * (1 - oh) * sm)

        # Update weights for output units
        for j, unit in enumerate(self.output_layer):
            for i, weight in enumerate(unit):
                x = hidden_results[i - 1] if i != 0 else 1.0
                delta = self.learnrate * output_errors[j] * x
                self.output_layer[j][i] = weight + delta

        # Update weights for hidden units
        for j, unit in enumerate(self.hidden_layer):
            for i, weight in enumerate(unit):
                x = input_values[i - 1] if i != 0 else 1.0
                delta = self.learnrate * hidden_errors[j] * x
                self.hidden_layer[j][i] = weight + delta

    @staticmethod
    def net(input: List[float], unit: List[float]):
        return sum(w * x for w, x in zip(unit, [1, *input]))


    @staticmethod
    def sigmoid(y):
        return 1 / (1 + euler**(-y))


    @staticmethod
    def from_file(
        filename: str,
        *,
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


    @staticmethod
    def training_samples_from_file(filename: str) -> List[Tuple[List[float], List[float]]]:
        samples = []

        with open(filename, "r") as infile:
            for line in (line.strip() for line in infile):
                inp, out = [list(map(float, s.split(" "))) for s in line.split("  ")]
                samples.append((inp, out))

        return samples
