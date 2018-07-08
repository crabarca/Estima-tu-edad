from scipy import ndimage
from model import model

import os
import numpy as np

print('Load Images')
x_test = np.empty((280, 110, 90))
y_test = np.empty((280, 1))
for file in os.listdir('test_folder'):
  np.append(x_test, ndimage.imread('test_folder/' + file))
  np.append(y_test, int(file.split('_')[1]))

x_train = np.empty((100, 110, 90))
y_train = np.empty((100, 1))
count = 0
for file in os.listdir('train_folder'):
  if count < 100:
    np.append(x_train, ndimage.imread('train_folder/' + file))
    np.append(y_train, int(file.split('_')[1]))
  count += 1

print('Fit model')

model.fit(np.asarray(x_train),
          np.asarray(y_test),
          epochs=20,
          batch_size=128,
          verbose=1)

score = model.evaluate(x_test, y_test, batch_size=128)

