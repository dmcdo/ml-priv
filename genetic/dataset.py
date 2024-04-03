from attr import AttributeDefinition
from individual import Individual
from typing import Dict, List

class DataSet:
    samples: List[Dict[str, str]] = []

    def __init__(self, dataset: str, kind: str, attr: AttributeDefinition) -> None:
        with open(f"{dataset}-{kind}.txt", "r") as infile:
            lines = [line.strip() for line in infile.readlines() if line.strip()]

        for line in lines:
            sample = {}

            for attrName, attrValue in zip((*attr.order, attr.target_attr), line.split()):
                sample[attrName] = attrValue

            self.samples.append(sample)
