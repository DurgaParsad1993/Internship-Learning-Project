# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ptyjQa1PN23AwGJ0Ydc77poS4g6LAhSK
"""

import pandas as pd
Diab = pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Diabetes.csv')
# Diab.head(5)
# Diab.info()
# Diab.describe()
# Diab.columns
Y = Diab ['diabetes']
X = Diab [['pregnancies', 'glucose', 'diastolic', 'triceps', 'insulin', 'bmi','dpf', 'age']]
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,train_size = 0.7,random_state = 2529)

# X_train.shape, X_test.shape, Y_train.shape, Y_test.shape

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter = 500)

model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(Y_test,Y_pred)