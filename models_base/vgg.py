import keras

def vgg16(image_shape=(480, 480, 3), trainable=False):
    efficientNetV2L = keras.applications.VGG16(
        weights='imagenet',
        include_top=False,
        input_shape=image_shape
    )
    
    efficientNetV2L.trainable = trainable
    
    return efficientNetV2L