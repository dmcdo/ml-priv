from typing import Optional, List
from random import choice, randint, sample

from attr import AttributeDefinition


class Rule:
    attr: AttributeDefinition = None

    def __init__(self) -> None:
        self.preconditions: List[List[str]] = []
        self.postcondition: str = None

    @staticmethod
    def random_from_attr(attr: AttributeDefinition) -> "Rule":
        rule = Rule()
        rule.attr = attr

        # Initialize random preconditions
        for attrVals in attr.attributes.values():
            rule.preconditions.append(sample(attrVals, k=randint(1, len(attrVals))))

        # Initialize random postcondition
        rule.postcondition = choice(attr.target_vals)

        return rule

    def __str__(self) -> str:
        return " ^ ".join(f"({' v '.join(i) or 'FALSE'})" for i in self.preconditions) + f" => {self.postcondition}"


class Hypothesis:
    attr: AttributeDefinition = None

    def __init__(self):
        self.rules: List[Rule] = []
        self.default: Rule = None

    @staticmethod
    def random_from_attr(attr: AttributeDefinition) -> "Hypothesis":
        hypothesis = Hypothesis()
        while randint(0, 1):
            hypothesis.rules.append(Rule.random_from_attr(attr))

        hypothesis.default = choice(attr.target_vals)

        return hypothesis

    def answer(self, sample: List[str]) -> str:
        for rule in self.rules:
            if all(val in allowed for allowed, val in zip(rule.preconditions, sample)):
                return rule.postcondition

        return self.default

    def __str__(self) -> str:
        return "\n".join(str(rule) for rule in self.rules) + f"\nTRUE => {self.default}"
