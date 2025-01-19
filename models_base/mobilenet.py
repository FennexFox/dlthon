import keras

def MV2(image_shape=(224, 224, 3), trainable=False):
    mobilenetV2 = keras.applications.MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=image_shape
    )
    
    mobilenetV2.trainable = trainable
    
    return mobilenetV2