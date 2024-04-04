from attr import AttributeDefinition
from hypothesis import Hypothesis
from typing import List
from sample import SampleSet


def fitness(h: Hypothesis, S: SampleSet):
    return len(list(filter(bool, (h.answer(s) == s[-1] for s in S.samples)))) / len(S.samples)

def GA(
    attr: AttributeDefinition,
    t: float,
    p: List[Hypothesis],
    S: SampleSet,
) -> Hypothesis:
    P = [Hypothesis.random_from_attr(attr) for _ in range(p)]
    F = [fitness(h, S) for h in P]

    while max(F) < t:
        pass