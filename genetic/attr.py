import typing


class AttributeDefinition:
    # Class variables
    CONTINUOUS = ["continuous"]

    # Instance variables
    attributes: typing.Dict[str, typing.List[str]] = {}
    target_attr: str
    target_vals: typing.List[str]

    def __init__(self, dataset: str) -> None:
        filename = f"{dataset}-attr.txt"

        with open(filename, "r") as fin:
            lines = [l.strip() for l in fin.readlines() if l.strip()]

            for line in lines[:-1]:
                attr, *values = line.split()

                if values == AttributeDefinition.CONTINUOUS:
                    self.attributes[attr] = []  # TODO
                else:
                    self.attributes[attr] = values

            self.target_attr, *self.target_vals = lines[-1].split()

    def __str__(self) -> str:
        builder = []

        for attribute, values in self.attributes.items():
            builder.append(attribute + " " + " ".join(values))        
        builder.append("")
        builder.append(self.target_attr + " " + " ".join(self.target_vals))
        builder.append("")
        
        return "\n".join(builder)

        