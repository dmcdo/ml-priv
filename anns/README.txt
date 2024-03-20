Instructions:
The main program is to be called with `python3 main.py`
The main program accepts the following arguments:
    -d :: Data set. ie, identity, tennis, or iris. (default identity)
    -n :: Number of hidden units (default 3)
    -l :: Learning Rate (default 0.3)
    -m :: Momentum (default 0.3)
    -e :: Epochs (default 5000)
    --show-propagation :: When raised, display the hidden values calculated
                          when checking the accuracy of the ANN against the
                          training and testing data.

i. testIdentity
$ python3 main.py -d identity -n 3 --show-propagation
$ python3 main.py -d identity -n 4 --show-propagation

ii. testTennis
$ python3 main.py -d tennis

iii. testIris
$ python3 main.py -d iris

iv. testIrisNoisy
$ python3 test_iris_noisy.py

    - Note: For test_iris_noisy.py, the "-d" and "--show-propagation" arguments to not work.