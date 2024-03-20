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
        num_input_values: int,
        num_output_values: int,
        learnrate: float,
        momentum: float,
        num_hidden_units: int,
        input_encoding: Optional[List[List[str]]] = None,
        output_encoding: Optional[List[List[str]]] = None,
    ):
        """
        Initialization method.
        """
        # Constants
        self.learnrate = float(learnrate)
        self.momentum = float(momentum)

        # For momentum
        self.prev_output_deltas = None
        self.prev_hidden_deltas = None

        # 1-of-n encoding
        if input_encoding is None:
            self.input_encoding = [None for _ in range(num_input_values)]
        else:
            self.input_encoding = input_encoding

        if output_encoding is None:
            self.output_encoding = [None for _ in range(num_output_values)]
        else:
            self.output_encoding = output_encoding

        # Compensate for 1-of-n
        num_input_values = sum(len(e) if e is not None else 1 for e in self.input_encoding)
        num_output_values = sum(len(e) if e is not None else 1 for e in self.output_encoding)

        # Create layers
        self.hidden_layer = [random_weights(num_input_values + 1) for _ in range(num_hidden_units)]
        self.output_layer = [random_weights(num_hidden_units + 1) for _ in range(num_output_values)]

    def debug_print(self):
        """
        Print all units for each layer.
        """
        print(self.hidden_layer)
        print(self.output_layer)


    def propagate(self, input_values: List[float]) -> List[List[float]]:
        # 1-of-n encode input
        input_values = self.encode_input_values(input_values)

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
        # Propagate sample through network
        hidden_results, output_results = self.propagate(input_values)

        # 1-of-n encode
        input_values = self.encode_input_values(input_values)
        target_values = self.encode_output_values(target_values)

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

        # Update output units
        output_deltas = []
        for j, unit in enumerate(self.output_layer):
            output_deltas.append([])

            # For each weight in the output layer
            for i, weight in enumerate(unit):
                x = hidden_results[i - 1] if i != 0 else 1.0

                if self.prev_output_deltas is None:
                    delta = self.learnrate * output_errors[j] * x
                else:
                    delta = self.learnrate * output_errors[j] * x + self.momentum * self.prev_output_deltas[j][i]

                # Update
                self.output_layer[j][i] = weight + delta
                output_deltas[j].append(delta)

        # Update hidden units
        hidden_deltas = []
        for j, unit in enumerate(self.hidden_layer):
            hidden_deltas.append([])

            # For each weight in the hidden layer
            for i, weight in enumerate(unit):
                x = input_values[i - 1] if i != 0 else 1.0

                if self.prev_hidden_deltas is None:
                    delta = self.learnrate * hidden_errors[j] * x
                else:
                    delta = self.learnrate * hidden_errors[j] * x + self.momentum * self.prev_output_deltas[j][i]

                # Update
                self.hidden_layer[j][i] = weight + delta
                hidden_deltas.append(delta)


    def compute_accuracy(
        self,
        training_samples: List[Tuple[List[float], List[float]]],
    ) -> float:
        for training_sample in training_samples:
            input_values, target_values = training_sample


    def encode_input_values(self, input_values) -> List[float]:
        encoded_input_values = []
        for i in range(len(input_values)):
            if self.input_encoding[i] is None:
                encoded_input_values.append(float(input_values[i]))
            else:
                for discrete_value in self.input_encoding[i]:
                    if discrete_value == input_values[i]:
                        encoded_input_values.append(1.0)
                    else:
                        encoded_input_values.append(0.0)

        return encoded_input_values


    def encode_output_values(self, output_values) -> List[float]:
        encoded_output_values = []
        for i in range(len(output_values)):
            if self.output_encoding[i] is None:
                encoded_output_values.append(float(output_values[i]))
            else:
                for discrete_value in self.output_encoding[i]:
                    if discrete_value == output_values[i]:
                        encoded_output_values.append(1.0)
                    else:
                        encoded_output_values.append(0.0)

        return encoded_output_values


    def decode_output_values(self, output_values) -> List[str]:
        i = 0
        results = []

        for encoding in self.output_encoding:
            if encoding is None:
                results.append(str(int(round(output_values[i]))))
                i += 1
            else:
                result = encoding[max(enumerate(output_values[i:i + len(encoding)]), key=lambda x: x[1])[0]]
                results.append(result)
                i += len(encoding)

        return results

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
    ) -> "ANN":
        with open(filename, "r") as infile:
            lines = [line.strip() for line in infile]

        if lines[0].startswith("in1:"):
            split_pnt = lines.index("")
            inp_lines = lines[:split_pnt]
            out_lines = lines[split_pnt + 1:]

            return ANN(
                len(inp_lines),
                len(out_lines),
                learnrate,
                momentum,
                num_hidden_units,
            )
        else:
            split_pnt = lines.index("")
            inp_lines = lines[:split_pnt]
            out_lines = lines[split_pnt + 1:]

            # 1-of-n encode discrete features
            input_encoding = []
            for line in inp_lines:
                name, *values = line.split(" ")
                if values == ["continuous"]:
                    input_encoding.append(None)
                else:
                    input_encoding.append(values)

            output_encoding = []
            for line in out_lines:
                name, *values = line.split(" ")
                if values == ["continuous"]:
                    output_encoding.append(None)
                else:
                    output_encoding.append(values)

            return ANN(
                len(inp_lines),
                len(out_lines),
                learnrate,
                momentum,
                num_hidden_units,
                input_encoding,
                output_encoding,
            )


    @staticmethod
    def training_samples_from_file(
        filename: str,
    ) -> List[Tuple[List[float], List[float]]]:
        samples = []

        with open(filename, "r") as infile:
            lines = [line.strip() for line in infile]

        if "  " in lines[0]:
            for line in lines:
                inp, out = [s.split(" ") for s in line.split("  ")]
                samples.append((inp, out))
        else:
            for line in lines:
                *inp, out = line.split(" ")
                samples.append((inp, [out]))

        return samples
