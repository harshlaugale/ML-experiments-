# -*- coding: utf-8 -*-
"""expt6_211P038_harshla.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y6fbFpGb3RmUPGLcBk32VVwSE09u90zM
"""

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# Generate a synthetic dataset
X, y = make_classification(n_samples=10000, n_features=10, n_informative=3, random_state=42)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Bagging Classifier with Decision Tree as base estimator
# The base_estimator argument has been replaced with estimator
bagging_classifier = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=500,
    max_samples=0.5,
    bootstrap=True,
    random_state=42
)

# Train the model
bagging_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = bagging_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

from sklearn import datasets

boston = datasets.load_boston() # dataset loadboston
X_boston, Y_boston = boston.data, boston.target
print('Dataset features names : '+ str(boston.feature_names)) # coulmn name
print('Dataset features size : '+ str(boston.data.shape))  # 13 input column
print('Dataset target size : '+ str(boston.target.shape))   # 1 output column

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X_boston, Y_boston , train_size=0.80, test_size=0.20, random_state=123)
print('Train/Test Sets Sizes : ',X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)
# 404 in training and 102 in testing

lr = LinearRegression()
dt = DecisionTreeRegressor()
knn = KNeighborsRegressor()

"""***Random Forest***"""

import pandas as pd
from sklearn.datasets import load_digits # load dogits dataset
digits = load_digits()

dir(digits) # propertiesm

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt

plt.gray()
for i in range(4):
    plt.matshow(digits.images[i])

df = pd.DataFrame(digits.data)
df.head()
# each sample is an array of 64 samples

df['target'] = digits.target

X = df.drop('target',axis='columns')
y = df.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

len (X_test)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=20) # change estimator upto 40 check scorre
model.fit(X_train, y_train)

model.score(X_test, y_test)

y_predicted = model.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
cm

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')