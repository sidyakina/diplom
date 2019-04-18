from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import plot_model

dataset = np.loadtxt("test\examples.txt", delimiter=",")
X = dataset[:, 10:]
inputDim = len(X[0])
Y = dataset[:, :10]


dataset = np.loadtxt("test\examplesTest.txt", delimiter=",")
X_test = dataset[:, 10:]
Y_test = dataset[:, :10]


model = Sequential()
model.add(Dense(24, input_dim=inputDim, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
history = model.fit(X, Y, epochs=20, batch_size=500, verbose=2, validation_split=0.2)
print(model.evaluate(X_test, Y_test, batch_size=2))
print(model.evaluate(X, Y, batch_size=2))

# plot_model(model, to_file='model.png', show_shapes=True)

model_yaml = model.to_yaml()
yaml_file = open("nn_model.yml", "w")
yaml_file.write(model_yaml)
yaml_file.close()
model.save_weights("nn_model.h5")


dataset = np.loadtxt("test\examplenumbers.txt", delimiter=",")
print(dataset)
print(model.predict(dataset))


# График точности модели
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# График оценки loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


