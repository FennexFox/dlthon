from keras import layers

def top1(base):
    x = layers.Flatten()(base)
    x = layers.Dense(256, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    
    return x

def top2(base):
    x = layers.GlobalAveragePooling2D()(base)
    x = layers.Dense(256, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(256, activation='relu')(x)
    
    return x

def top3(base):
    x = layers.GlobalAveragePooling2D()(base)
    x = layers.Dense(512, activation='relu')(x)
    x = layers.Dense(512, activation='relu')(x)
    x = layers.Dropout(0.5)(x)
    x = layers.Dense(256, activation='relu')(x)
    
    return x