from scipy import ndimage
from model import model
from keras.utils import to_categorical
from keras.models import load_model

import os
import numpy as np

print('Load Images')
x_test = np.empty((280, 110, 90))
y_test = np.empty((280, 1))
index = 0
for i in range(7):
    for j in range(1, 41):
        image = ndimage.imread('train_folder/face_{}_{}.jpg'.format(str(i + 1).zfill(3), str(j).zfill(5)))
        np.append(x_test, image)
        y_test[index] = i
        index += 1


x_train_array = np.load('x_train.npy')
y_train_array = np.load('y_train.npy')

print('Fit model')

if not os.path.exists('my_model-two.h5'):
    model.fit(x_train_array,
              y_train_array,
              epochs=10,
              batch_size=128,
              verbose=1)
    model.save('my_model-two.h5')
else:
    model = load_model('my_model-two.h5')

print('Evaluate')
x_test_array = np.expand_dims(np.asarray(x_test), axis=3)
y_test_array = to_categorical(y_test, num_classes=7)

# score = model.evaluate(x_test_array, y_test_array, batch_size=128)
print(x_test_array[0].shape)
score = model.predict(x_test_array)
print(score)

