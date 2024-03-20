from tempfile import TemporaryDirectory
from pathlib import Path
import shutil
import random
import main
import argparse
import subprocess
import sys


for corruption_percent in [i / 100 for i in range(2, 21, 2)]:
    with TemporaryDirectory() as tempdir:
        # We will move these to the temporary directory since they will be unchanged
        shutil.copy(f"iris-attr.txt", Path(tempdir, "iris-attr.txt"))
        shutil.copy(f"iris-test.txt", Path(tempdir, "iris-test.txt"))
        shutil.copy(f"iris-train.txt", Path(tempdir, "iris-train-uncorrupted.txt"))

        with open("iris-train.txt", "r") as infile:
            lines = [line.strip() for line in infile if line.strip()]

        # Determine how much corruption to do.
        num_corrupted_samples = int(round(corruption_percent * len(lines)))
        indexes_of_corruped_samples = set(random.sample(range(len(lines)), num_corrupted_samples))

        # Do corruption
        with open(Path(tempdir, "iris-train.txt"), "w") as outfile:
            for i, line in enumerate(lines):
                if i in indexes_of_corruped_samples:
                    *inp, out = line.split(" ")
                    inp = " ".join(inp)
                    out = random.choice(list({"Iris", "Iris-setosa", "Iris-versicolor", "Iris-virginica"}.difference({out})))
                    outfile.write(f"{inp} {out}\n")
                else:
                    outfile.write(f"{line}\n")

        # Grab some arguments
        parser = argparse.ArgumentParser()
        parser.add_argument("-n", "--num-hidden-units", type=int, default=3)
        parser.add_argument("-l", "--learn-rate", type=float, default=0.3)
        parser.add_argument("-m", "--momentum", type=float, default=0.3)
        parser.add_argument("-e", "--epochs", type=int, default=500)
        arguments = parser.parse_args()

        print(f"With {100 * corruption_percent}% corruption:")
        subprocess.run([
            sys.executable,
            Path(__file__).absolute().parent / "main.py",
            "-d", "iris",
            "-n", str(arguments.num_hidden_units),
            "-l", str(arguments.learn_rate),
            "-m", str(arguments.momentum),
            "-e", str(arguments.epochs),
        ], cwd=tempdir)

        print()


