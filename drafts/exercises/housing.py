#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 18:58:25 2019

@author: itamar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("datasets/housing.csv")

splitting = dataset[dataset['total_bedrooms'].isnull()]
X_substituingtotal_bedrooms = splitting.iloc[:,3:4].values

dataset = dataset.dropna(how = 'any')
dataset['total_bedrooms'].isnull().sum()

X_train = dataset.iloc[:,3:4].values
y_train = dataset.iloc[:,4].values

from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
y_train = y_train.reshape(-1,1)
y_train = scaler.fit_transform(y_train)

regressor = SVR()
regressor.fit(X_train,y_train)
y_pred = regressor.predict(X_substituingtotal_bedrooms)

splitting['total_bedrooms'] = y_pred

dataset = dataset.append(splitting)


from sklearn.preprocessing import LabelEncoder ,OneHotEncoder
encoder = LabelEncoder()
dataset['ocean_proximity'] = encoder.fit_transform(dataset['ocean_proximity'])
OneHotEncoder = OneHotEncoder(categorical_features=[9])
dataset = OneHotEncoder.fit_transform(dataset).toarray()

dataset = pd.DataFrame(dataset)
dataset = dataset.drop(columns = 2)


#pd.plotting.scatter_matrix(dataset, figsize=(6, 6))
#plt.show()

#plt.matshow(dataset.corr())
#plt.xticks(range(len(dataset.columns)), dataset.columns)
#plt.yticks(range(len(dataset.columns)), dataset.columns)
#plt.colorbar()
#plt.show()

y = dataset.iloc[:,12].values
X = dataset.drop(columns = [12]).values

from sklearn.preprocessing import StandardScaler, RobustScaler
scaler = RobustScaler()
X = scaler.fit_transform(X)
"""
need to use different scaler types and compare
"""

from sklearn.decomposition import PCA
pca = PCA(n_components = 6)
X = pca.fit_transform(X)
explained_variance = pca.explained_variance_ratio_.sum()

from sklearn.model_selection import train_test_split
X_train,X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X_train,y_train)
y_pred = regressor.predict(X_test)

from sklearn.ensemble import RandomForestRegressor
regressor2 = RandomForestRegressor(n_estimators=10,n_jobs=-1)
regressor2.fit(X_train,y_train)
y_pred2 = regressor2.predict(X_test)

from sklearn.metrics import r2_score, explained_variance_score
print('Decision tree\n r2_score:',r2_score(y_test,y_pred),'\nvariance : ',explained_variance_score(y_test,y_pred))
print('Random Forest\n r2_score:',r2_score(y_test,y_pred2),'\nvariance : ',explained_variance_score(y_test,y_pred2))
"""
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = regressor, X = X, y = y, cv = 10,n_jobs=-1)
accuracies.mean()


from sklearn.model_selection import GridSearchCV
parameters = [{'n_estimators': [2,4,5,8,10,15,17],'criterion': ['mse']},
              {'n_estimators': [2,4,5,8,10,15,17],'criterion': ['mae']}]
grid = GridSearchCV(estimator = regressor2,
                    param_grid= parameters,
                    cv = 10,
                    n_jobs=-1)


from sklearn.model_selection import GridSearchCV
params=[{
            'n_estimators':[20,200,680],
            'max_depth':[10,50,100]
            
            
        }]

grid = GridSearchCV(estimator = regressor2,
                    param_grid= params,
                    cv = 2,
                    scoring = 'r2',
                    n_jobs=-1)


grid = grid.fit(X_train,y_train)
best_accuracy = grid.best_score_
best_parameters = grid.best_params_
print(best_parameters)
print(best_accuracy)
"""