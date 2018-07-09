import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Conv2D, MaxPool2D, Flatten, Input
from keras.optimizers import SGD

model = Sequential()
<<<<<<< HEAD
model.add(Conv2D(32, 7, activation='relu', input_shape=(110, 90, 1), data_format='channels_last'))
=======
model.add(Conv2D(32, 7, activation='relu', input_shape=(110, 90, 3)))
>>>>>>> 793e297acee6ca5b92b0773202c756dc10b8b4c8
model.add(MaxPool2D(strides=2))
model.add(Conv2D(64, 7, activation='relu'))
model.add(MaxPool2D(strides=2))
model.add(Conv2D(128, 3, activation='relu'))
model.add(MaxPool2D(strides=2))
model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dense(7, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['categorical_accuracy'])

<<<<<<< HEAD
if __name__ == '__main__':
    print(model.summary())
=======
model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)
>>>>>>> 793e297acee6ca5b92b0773202c756dc10b8b4c8


