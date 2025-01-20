import tensorflow, keras
from keras import layers

def image_preprocessing_v1():
    return keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.2),
        layers.RandomTranslation(0.1, 0.1),
        layers.RandomZoom(0.2),
        
        layers.Rescaling(1./255),
    ])
    
def image_preprocessing_v2():
    return keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.2),
        layers.RandomTranslation(0.1, 0.1),
        layers.RandomZoom(0.2),
        
        layers.BatchNormalization(),
    ])