import os
import numpy as np
from scipy import ndimage
from keras.utils import to_categorical

n_samples = len(os.listdir('train_color_20k'))
x_train = np.empty((9800, 110, 90, 3))
y_train = np.empty((9800, 1))

index = 0
for i in range(7):
    for j in range(1, 1401):
        print('Label {}, image {}'.format(str(i + 1).zfill(3), str(j).zfill(5)))
        image = ndimage.imread('train_color_20k/face_{}_{}.jpg'.format(str(i + 1).zfill(3), str(j).zfill(5)))
        np.append(x_train, image)
        y_train[index] = i
        index += 1


# x_train_array = np.expand_dims(np.asarray(x_train), axis=3)
y_train_array = to_categorical(y_train, num_classes=7)

np.save('x_train_color', x_train)
np.save('y_train_color', y_train_array)

