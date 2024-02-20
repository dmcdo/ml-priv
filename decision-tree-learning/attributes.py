class Attributes:
    __slots__ = ("order", "attrs", "target", "targetvals")

    def __init__(self, fname: str):
        self.order = []
        self.attrs = {}
        with open(fname, "r") as attrfile:
            while True:
                line = attrfile.readline().strip()
                if line == "":
                    break

                key, *vals = line.split()
                self.order.append(key)
                self.attrs[key] = vals

            self.target, *self.targetvals = attrfile.readline().strip().split()


Wh