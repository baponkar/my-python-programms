from worldometer import Worldometer
import matplotlib.pyplot as plt


x = 0

w = Worldometer().metrics_with_labels()['births_this_year']

print(w)
