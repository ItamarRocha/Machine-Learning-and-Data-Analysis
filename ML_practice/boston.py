#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 07:56:44 2019

@author: itamar
"""

from keras.datasets import boston_housing

(train_data, train_targets) , (test_data,test_targets) = boston_housing.load_data()

mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std
test_data -= mean
test_data /= std

from keras import models
from keras import layers
    
#print(train_data.shape[1])
def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64,activation='relu',input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64,activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer ='rmsprop',loss='mse', metrics=['mae'])
    return model
#last layer can predict any value. It wouldnt make sense to put an activation as sigmoid as we dont want a probability
"""
Note that you compile the network with the mse loss function—mean squared error,
the square of the difference between the predictions and the targets. This is a widely
used loss function for regression problems.
You’re also monitoring a new metric during training: mean absolute error ( MAE ). It’s
the absolute value of the difference between the predictions and the targets. For
instance, an MAE of 0.5 on this problem would mean your predictions are off by $500
on average.
"""
#does not makes sense to use validation set in this example cause we have too little data


import numpy as np
from sklearn.metrics import r2_score
k = 4
num_val_samples = len(train_data) // k
num_epochs = 100
all_scores = []
all_r2 = []

for i in range(k):
    print('processing fold #',i)
#    -----------|i|=====|i +1|-------------
    val_data = train_data[i*num_val_samples: (i+1)*num_val_samples]
    val_targets = train_targets[i*num_val_samples: (i+1)*num_val_samples]
    
    partial_train_data = np.concatenate(
            [train_data[:i * num_val_samples],
             train_data[(i + 1) * num_val_samples:]],
             axis=0)
    
    partial_train_targets = np.concatenate(
            [train_targets[:i * num_val_samples],
             train_targets[(i + 1) * num_val_samples:]],
             axis=0)
    
    model = build_model()
    model.fit(partial_train_data,partial_train_targets,
              epochs = num_epochs, batch_size=1, verbose=0)
    val_mse, val_mae = model.evaluate(val_data,val_targets,verbose=0)
    all_r2.append(r2_score(val_targets,model.predict(val_data)))
    all_scores.append(val_mae)
    
num_epochs = 500
all_mae_histories = []
all_r2_500 = []
for i in range(k):
    print('processing folf #',i)
    val_data = train_data[i*num_val_samples: (i+1)*num_val_samples]
    val_targets = train_targets[i*num_val_samples: (i+1)*num_val_samples]
    
    partial_train_data = np.concatenate(
            [train_data[:i * num_val_samples],
             train_data[(i + 1) * num_val_samples:]],
             axis=0)
    
    partial_train_targets = np.concatenate(
            [train_targets[:i * num_val_samples],
             train_targets[(i + 1) * num_val_samples:]],
             axis=0)
    
    model = build_model()
    history = model.fit(partial_train_data,partial_train_targets,
              epochs = num_epochs, batch_size=1, verbose=0)
    val_mse, val_mae = model.evaluate(val_data,val_targets,verbose=0)
    all_r2_500.append(r2_score(val_targets,model.predict(val_data)))
    mae_history = history.history['mae']
    all_mae_histories.append(mae_history)


average = [np.mean([x[i]for x in all_mae_histories]) for i in range(num_epochs)]

import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(range(1, len(average) + 1), average)
plt.xlabel('Epochs')
plt.ylabel('Validation MAE')
plt.show()

def smooth_curve(points, factor=0.9):
    smoothed_points = []
    for point in points:
            if smoothed_points:
                previous = smoothed_points[-1]
                smoothed_points.append(previous * factor + point * (1 - factor))
            else:
                smoothed_points.append(point)
    return smoothed_points

smooth_mae_history = smooth_curve(average[10:])
plt.figure(2)
plt.plot(range(1, len(smooth_mae_history) + 1), smooth_mae_history)
plt.xlabel('Epochs')
plt.ylabel('Validation MAE')
plt.show()

#after finishing tunning all parameters implement final model with
#al optimizations 

final_model = build_model()
final_model.fit(train_data,train_targets,
                epochs = 80, batch_size=16,verbose=0)
test_mse_score, test_mae_score = model.evaluate(test_data,test_targets)