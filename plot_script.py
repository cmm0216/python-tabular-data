#!/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
dataframe = pd.read_csv("iris.csv")
x = dataframe.petal_length_cm
y = dataframe.sepal_length_cm
color = {"Iris_setosa": 'red', "Iris_versicolor": 'blue', "Iris_virginica": 'green'}
species = dataframe.species
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
#plt.scatter(x, y, label = 'Data', c = dataframe.species.map(color))
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("petal_v_sepal_length_species_regress.png")
quit()