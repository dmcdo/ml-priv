PYTHON=python3

testTennis:
	$(PYTHON) learn.py tennis-attr.txt tennis-train.txt tennis-tree.pkl
	$(PYTHON) judge.py tennis-attr.txt tennis-train.txt tennis-test.txt tennis-tree.pkl
	$(PYTHON) printer.py tennis-tree.pkl

testBool:
	$(PYTHON) learn.py bool-attr.txt bool-train.txt bool-tree.pkl
	$(PYTHON) judge.py bool-attr.txt bool-train.txt bool-test.txt bool-tree.pkl
	$(PYTHON) printer.py bool-tree.pkl

testIris:
	$(PYTHON) learn.py iris-attr.txt iris-train.txt iris-tree.pkl
	$(PYTHON) judge.py iris-attr.txt iris-train.txt iris-test.txt iris-tree.pkl
	$(PYTHON) printer.py iris-tree.pkl

clean:
	rm -f *.pkl
