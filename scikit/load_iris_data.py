import numpy as np
import scipy as sp
import mglearn
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris


iris_dataset = load_iris()

print("keys of datasets :{}".format(iris_dataset.keys()))
print(iris_dataset['DESCR'])
