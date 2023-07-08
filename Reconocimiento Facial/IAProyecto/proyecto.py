# codifica una red nueronal que ya este entrenada para la deteccion de colores
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

# Definir el modelo de red neuronal
model = Sequential()
# Capa de entrada con 3 neuronas (RGB)
model.add(Dense(32, activation='relu', input_dim=3))
model.add(Dense(64, activation='relu'))  # Capa oculta con 64 neuronas
model.add(Dropout(0.5))  # Agregar un dropout para evitar overfitting
# Capa de salida con 10 neuronas (10 colores)
model.add(Dense(10, activation='softmax'))
# Compilar el modelo
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9,
          nesterov=True)  # Definir el optimizador
# Compilar el modelo con la función de pérdida y el optimizador definido previamente
model.compile(loss='categorical_crossentropy', optimizer=sgd)
# Entrenar la red neuronal con los datos de entrenamiento
# Entrenar la red neuronal con los datos de entrenamiento
model.fit(X_train, y_train, epochs=20, batch_size=32)

# como instalar tensorflow

