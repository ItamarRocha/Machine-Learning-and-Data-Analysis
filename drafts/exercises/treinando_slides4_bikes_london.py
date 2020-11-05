#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:19:54 2019
@author: itamar
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("datasets/london_merged.csv")#,decimal = ",")

dataset['timestamp'] = pd.to_datetime(dataset['timestamp'])

dataset['day'] = dataset['timestamp'].dt.day
dataset['month'] = dataset['timestamp'].dt.month
dataset['hour'] = dataset['timestamp'].dt.hour

dataset = dataset.drop(columns = ['timestamp'])

dataset.isnull().sum()
dataset.duplicated()

stats = dataset.describe(include = "all")
#sns.pairplot(dataset)

"""
#corr = dataset.corr()

plt.boxplot(dataset['cnt'])
plt.title('boxplot')
plt.xlabel('cnt')
plt.ylabel('valores')
plt.ticklabel_format(style='sci', axis='y', useMathText = True)

dataset['cnt'].mean()

pd.plotting.scatter_matrix(dataset, figsize=(12, 12))
plt.show()
"""

X = dataset.iloc[:,1:13].values
y = dataset.iloc[:,0].values

from sklearn.preprocessing import  MinMaxScaler,StandardScaler,RobustScaler
sc= StandardScaler()
X= sc.fit_transform(X)
y= y.reshape(-1,1)
y=sc.fit_transform(y)

"""
from sklearn.preprocessing import StandardScaler
X = StandardScaler().fit_transform(X)
"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state = 0,test_size = 0.2)

"""
#1.Linear regressor
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
#2. Support vector regression machine regressor
from sklearn.svm import SVR
regressor = SVR(kernel='rbf')

#3. Decision tree
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()

#4. RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators= 10)
regressor.fit(X_train, y_train)

#5. import sklearn
from sklearn.neighbors import KNeighborsRegressor
regressor = KNeighborsRegressor(n_neighbors= 2)
regressor.fit(X_train,y_train)
#sorted(sklearn.neighbors.VALID_METRICS['brute'])
"""
from xgboost import XGBClassifier #fast and you dont need feature scalling
regressor = XGBClassifier()
regressor.fit(X_train, y_train.ravel())
y_pred = regressor.predict(X_test)

"""
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = regressor, X = X, y = y, cv = 10,n_jobs=-1)
accuracies.mean()
accuracies.std()

Metrics, in R2 best possible is 1. (can be negative,which is really bad)
in explained_variance_score the best possible is also two
max error -> best is 0 (its not working here)

    1.Linear Regression we obtained an r2_score of 0.3018994
and an explained_variance of 0.301962

    2.SVR obtained 0.15 r2 score and 0.23 explained variance
    
    3.In decisiontreeregressor we got an explained variance and and r2 of 0.9158
    
    4. In random forest we obtained 0.95 in each.
    
    5.KNN obtained both 0.59 with 3 neighbours with 5 got 0.60
"""

from sklearn import metrics
r2 = metrics.r2_score(y_test,y_pred)
explained_variance = metrics.explained_variance_score(y_test,y_pred)
#maxerr = max_error(y_test,y_pred)
"""
from sklearn.model_selection import GridSearchCV
parameters = [{'n_estimators': [5,10], 'criterion': ['mse']},
              {'n_estimators': [5,10], 'criterion': ['mae']}]
grid = GridSearchCV(estimator = regressor,
                    param_grid= parameters,
                    cv = 10,
                    n_jobs=-1)


grid = grid.fit(X_train,y_train)
best_accuracy = grid.best_score_
best_parameters = grid.best_params_
grid.best_estimator_
grid.best_index_
grid.cv_results_
"""
"""
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
"""