import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Conv2D, MaxPool2D, Flatten
from keras.optimizers import SGD

# Generate dummy data
import numpy as np
x_train = np.random.random((1000, 20))
y_train = keras.utils.to_categorical(np.random.randint(10, size=(1000, 1)), num_classes=10)
x_test = np.random.random((100, 20))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(100, 1)), num_classes=10)

model = Sequential()
model.add(Conv2D(32, 7, activation='relu', input_shape=(110, 90, 1)))
model.add(MaxPool2D(strides=2))
model.add(Conv2D(64, 7, activation='relu'))
model.add(MaxPool2D(strides=2))
model.add(Conv2D(128, 7, activation='relu'))
model.add(MaxPool2D(strides=2))
model.add(Flatten())
model.add(Dense(7, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])


# model.fit(x_train, y_train,
#           epochs=20,
#           batch_size=128)
# score = model.evaluate(x_test, y_test, batch_size=128)


