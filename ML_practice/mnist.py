#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 18:29:10 2019

@author: itamar
"""

from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images.shape
len(train_labels)
train_labels
test_images.shape
len(test_images)
test_labels

print(train_images.ndim)
train_images.shape
print(train_images.dtype)

digit = train_images[4]
import matplotlib.pyplot as plt
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()

from keras import models , layers

network = models.Sequential(name = 'hello Keras')
network.add(layers.Dense(512, activation = 'relu' , input_shape = (28*28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop',
loss='categorical_crossentropy',
metrics=['accuracy'])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_images, train_labels, epochs=20, batch_size=32)

test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc:', test_acc)

import numpy as np

x = np.array([[[1,2,3],
               [1,7,3],
               [1,2,3]],
              [[1,2,3],
               [1,4,3],
               [1,2,3]]])
x.ndim
x.shape

