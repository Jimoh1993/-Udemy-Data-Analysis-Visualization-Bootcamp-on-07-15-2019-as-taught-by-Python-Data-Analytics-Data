#Pckages Import
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#Create DataFrame by importing a new IRIS.csv file created from working directory
DataFrame = pd.read_csv("IRIS.csv")
print DataFrame



"""#Split the IRIS dataset into 2 subsets: Training Dataset (70% rows) and Testing Dataset (30% rows)
"""
#Split IRIS.csv Dataset into two subsets
flowers_features = DataFrame[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
flowers_classes = DataFrame[['Species']].values

#70% rows Train Dataset and 30% rows  Test Dataset  as shown below:
(train_flowers_features, test_flowers_features, train_flowers_classes, test_flowers_classes) = train_test_split(flowers_features, flowers_classes, train_size=0.7, test_size=0.3, random_state=0)

"""Implement the decision tree classifier algorithm 
on the IRIS Training dataset. Test the accuracy with Testing Dataset.
sklearn.tree python used
"""
DTC = DecisionTreeClassifier()
fitness = DTC.fit(train_flowers_features, train_flowers_classes)
accuracy = DTC.score(test_flowers_features, test_flowers_classes) #returns the mean accuracy on the given test dataset
# print fitness
print(accuracy)
print('The Accuracy of the Decision Tree Result is:' + str(accuracy * 100) + '%')
