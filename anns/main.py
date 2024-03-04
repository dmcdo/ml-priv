from ann import ANN, ann_from_file
import os
import os.path


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    ann = ann_from_file("identity-attr.txt")
    print(ann)