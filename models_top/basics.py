import tensorflow, keras
from keras import layers

def simple1():
    model = keras.Sequential([
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.5)
    ])
    return model

def simple2():
    model = keras.Sequential([
        layers.GlobalAveragePooling2D(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(256, activation='relu')
    ])
    return model

def midsize1():
    model = keras.Sequential([
        layers.GlobalAveragePooling2D(),
        layers.Dense(512, activation='relu'),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(256, activation='relu')
    ])
    return model