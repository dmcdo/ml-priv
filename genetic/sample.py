from attr import AttributeDefinition
from hypothesis import Hypothesis
from typing import Dict, List

class SampleSet:
    samples: List[List[str]] = None

    def __init__(self, dataset: str, kind: str) -> None:
        with open(f"{dataset}-{kind}.txt", "r") as infile:
            lines = [line.strip() for line in infile.readlines() if line.strip()]

        self.samples = [line.split() for line in lines]
