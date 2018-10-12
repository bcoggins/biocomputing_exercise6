# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 21:16:24 2018

@author: Bret
"""
#Excercise 6 Answers
#1 
#to get any number of head lines, change the lines variable
#to use a different file, change filename variable
import pandas as pd
filename = "wages.csv"
lines = 1
data=pd.read_csv(filename, header=0, sep=',' )
data.head(lines)


#2 
#print last 2 rows from last two columns of iris.csv
iris = pd.read_csv("iris.csv", header=0, sep=',')
iris.shape
print iris.loc[148:149,"Petal.Width":"Species"]
# number of observations per species
iris.Species.value_counts()

#get rows with sepal width greater than 3.5

iris[iris['Sepal.Width']>3.5]

#write all rows with setosa as csv file
setosa = iris[iris.Species == 'setosa' ]
setosa.to_csv('setosa.csv')
# calculate the mean, min, and max of Petal.length for virginica
virginica = iris[iris.Species == 'virginica' ]
virginica['Petal.Length'].min()
virginica['Petal.Length'].max()
virginica['Petal.Length'].mean()




