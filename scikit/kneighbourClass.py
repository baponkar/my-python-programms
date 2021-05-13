import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split



iris_datasets = load_iris()
print(iris_datasets.keys())

X_train,X_test,Y_train,Y_test = train_test_split(iris_datasets['data'],iris_datasets['target'],random_state = 0)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, Y_train)


X_new = np.array([[5, 2.9,1,0.2]])
prediction = knn.predict(X_new)

print(prediction)
print('Prediction be : {}'.format(iris_datasets.target_names[prediction]))

Y_prediction = knn.predict(X_test)

print(Y_prediction)

mean = np.mean(Y_prediction == Y_test)

print("The set score : {}".format(mean))
