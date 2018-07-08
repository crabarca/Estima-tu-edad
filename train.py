from scipy import ndimage
from model import model

import os
import numpy as np

length = len(os.listdir('train_folder'))
x_train = [ None for _ in range(length) ]
y_train = [ None for _ in range(length) ]
index = 0
print('Load Images')
for file in os.listdir('train_folder'):
  x_train[index] = ndimage.imread('train_folder/' + file)
  y_train[index] = int(file.split('_')[1])
  index += 1

length = len(os.listdir('test_folder'))
x_test = [ None for _ in range(length) ]
y_test = [ None for _ in range(length) ]
index = 0
for file in os.listdir('test_folder'):
  x_test[index] = ndimage.imread('test_folder/' + file)
  y_test[index] = int(file.split('_')[1])
  index += 1

print('Fit model')

model.fit(x_train, y_train,
          epochs=20,
          batch_size=128,
          verbose=1)

score = model.evaluate(x_test, y_test, batch_size=128)

print(score)
