#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:37:05 2020

@author: itamar
"""

from scipy.io import arff
import pandas as pd
import os
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
from sklearn.model_selection import GridSearchCV
os.path.exists('multilabel-classification-emotions')
emotions = arff.loadarff('multilabel-classification-emotions/emotions.arff')
emotions = pd.DataFrame(emotions[0])

emotions = emotions.astype(float)

X = emotions.iloc[:,0:72]
y = emotions.iloc[:,72:79]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2 ,random_state = 0)

y_trains = {}
y_tests = {}

cm = {}
cm_final = [[0 for x in range(2)] for y in range(2)] 
acc = {}
"""
grid = {}
parameters = [{'n_estimators': [80,90,100,110,120,130],'learning_rate': [0,0.05,0.1,0.9,1] }]
"""
y_finalpred = pd.DataFrame()

#classifier = RandomForestClassifier(n_estimators = 100, n_jobs = -1,verbose = 0)
classifier = XGBClassifier(n_estimators = 120,n_jobs = -1,)
#classifier = XGBClassifier()
#classifier = KNeighborsClassifier(n_neighbors = 7, n_jobs = -1)
for i , emots in zip(range(6),y_train.columns):
    y_trains[i] = pd.DataFrame(y_train.iloc[:,i:i+1])
    y_tests[i] = pd.DataFrame(y_test.iloc[:,i:i+1])
 
    classifier.fit(X_train,y_trains[i])
    y_pred = classifier.predict(X_test)
    """
    grid[i] = GridSearchCV(estimator = classifier,param_grid= parameters,cv = 10,n_jobs=-1)
    grid[i] = grid[i].fit(X_train,y_trains[i])
    
    best_accuracy = grid[i].best_score_
    best_parameters = grid[i].best_params_
    grid[i].best_estimator_
    grid[i].best_index_
    grid[i].cv_results_
    
    print(f"best_accuracy = {grid[i].best_score_} best_parameters = {best_parameters}")
    """
    cm[i] = confusion_matrix(y_tests[i],y_pred)
    cm_final += cm[i]
    acc[i] = accuracy_score(y_tests[i],y_pred)
    
    if not i:
        y_finalpred = pd.DataFrame(y_pred).rename({0:emots},axis = 'columns')
    else:
        y_finalpred = y_finalpred.join(pd.DataFrame(y_pred).rename({0:emots},axis = 'columns'))
    print(f"numero da coluna : {i} ACC = {acc[i]}")

print(f"final accuraccy = {(cm_final[0][0] + cm_final[1][1])/sum(sum(cm_final))}")

