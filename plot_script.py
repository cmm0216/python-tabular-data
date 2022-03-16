#!/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

print("This script will give you a plot of petal vs. sepal length.")

"""
Creates a scatter plot of petal vs septal length, that is color coded based on species, from an example file
given for n. 

Parameters
__________
	n: filename with quotes around it.
The name you type in is the name of the .csv file you;d like a plot for. Should match the same 
file setup as example file "iris.csv"

Returns
_______
A .png plot handmade special for you :)

Examples
________
>>> plotfile("iris.csv")
Then check working directory for a saved .png from the iris.csv file!
"""

def plotfile():
	iris = pd.read_csv(data)
	x = iris.petal_length_cm
	y = iris.sepal_length_cm
	color = {"Iris_setosa": 'red', "Iris_versicolor": 'blue', "Iris_virginica": 'green'}
	regression = stats.linregress(x, y)
	slope = regression.slope
	intercept = regression.intercept
	plt.scatter(x, y, label = 'Data', c = iris.species.map(color))
	plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
	plt.xlabel("Petal length (cm)")
	plt.ylabel("Sepal length (cm)")
	plt.legend()
	plt.savefig("petal_v_sepal_length_species_regress_Bestpractices2.png")

if __name__ == "__main__":
	plotfile()