from keras import layers

def simple_cnn(base):
    x = layers.Flatten()(base)
    x = layers.Dense(256, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    
    return x