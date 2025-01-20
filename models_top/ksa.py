import keras
from keras import layers

def ksa_simple1():
    model = keras.Sequential([
        layers.Conv2D(filters=32, kernel_size=3, activation="relu"),
        layers.MaxPooling2D(pool_size=2),
        layers.Conv2D(filters=64, kernel_size=3, activation="relu"),
        layers.MaxPooling2D(pool_size=2),
        layers.Conv2D(filters=128, kernel_size=3, activation="relu"),
        layers.MaxPooling2D(pool_size=2),
        layers.Conv2D(filters=256, kernel_size=3, activation="relu"),
        layers.MaxPooling2D(pool_size=2),
        layers.Conv2D(filters=256, kernel_size=3, activation="relu"),
        layers.Flatten(),
        layers.Dense(512, activation="relu"),
    ])
    
    model.name = "ksa_simple1"

    return model