from __future__ import print_function
import keras
import os
import scipy.io as sio
import numpy as np
import math
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.preprocessing.image import img_to_array, load_img
from keras import backend as K
from scipy import ndimage, misc



batch_size = 128
num_classes = 10
epochs = 2

# print(K.tensorflow_backend._get_available_gpus())

# input image dimensions
img_rows, img_cols = 28, 28
# img_rows, img_cols = 110, 90

def img_per_class(directory):
    ageRangeCounter = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    for filename in os.listdir(directory):
    # To count images per group when renamed
        group = int(filename.split("_")[1])
        ageRangeCounter[group] += 1
    
    totalSum = sum([v for k,v in ageRangeCounter.items()])
    print("Total sum: ", totalSum)
    print("Per class: ", ageRangeCounter)
    
    return ageRangeCounter

def set_data(directory):
    ageCounter = img_per_class(directory)
    x = []
    for filename in os.listdir('./datasets/train_folder'):
        img = load_img(os.path.join(directory, filename))
        img = img_to_array(img)
        x.append(img)
    # y = np.array([i for k,v in ageCounter.items() for i in range(v)])
    return x, y

(x,y) = set_data('datasets/train_folder')
print(x.shape)

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()


print(x_train.shape, y_train.shape)

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

# model.fit(x_train, y_train,
#           batch_size=batch_size,
#           epochs=epochs,
#           verbose=1,
#           validation_data=(x_test, y_test))
# score = model.evaluate(x_test, y_test, verbose=0)

# print('Test loss:', score[0])
# print('Test accuracy:', score[1])