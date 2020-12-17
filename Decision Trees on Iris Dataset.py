import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('Iris.csv')

#Check null value
df.isnull().any()

#Check Datatype of the flowers features
df.dtypes

#check a quick summary of dataset.
df.describe()

"""It seems most of summary data are pretty normal. 
Unless I notice that the PetalWidthCm have a weird value. 
It has a minimum value of 0.1 while the maximum one is actually 2.5. 
Let’s try to plot the PetalWithCm."""
df['PetalWidthCm'].plot.hist()
plt.show()


"""That seems very weird, about 50 flowers in this
 dataset have values between 0.1 and 0.5. Let’s check the file
 ."""

"""Check The Relationship Between Columns"""
sns.pairplot(df, hue='Species')


"""Splitting The Dataset"""
all_inputs = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
all_classes = df['Species'].values

"""Split the IRIS dataset into 2 subsets: Training Dataset (70% rows) and Testing Dataset (30% rows)"""
(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)


"""Classification with Decision Tree library from sklearn
Finally, we reach the last part that is the classification itself.
 We will use the decision tree classifier from the scikit-learn.
 The accuracy of our model achieves 95% without doing too much.
 """
dtc = DecisionTreeClassifier()
dtc.fit(train_inputs, train_classes)
dtc.score(test_inputs, test_classes)

#Added not part of it
DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1,
                       min_weight_fraction_leaf=0.0, max_features=None, random_state=None, max_leaf_nodes=None,
                       min_impurity_decrease=0.0, min_impurity_split=None, class_weight=None, presort=False)



