import numpy as np
import scipy as sp
import mglearn
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


iris_dataset = load_iris()
X_train, X_test, Y_train, Y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)


print("X_train shape :",X_train.shape)
print("X_test shape :",X_test.shape)

print("Y_train shape :",Y_train.shape)
print("Y_test shape :",Y_test.shape)


iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

pd.plotting.scatter_matrix(iris_dataframe, c=Y_train, figsize=(15,15),
        marker ='o',hist_kwds={'bins':20},s=60,alpha=.8,cmap=mglearn.cm3)
plt.show()






