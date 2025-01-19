import tensorflow as tf

def callback_savemodel(model_name):
    return tf.keras.callbacks.ModelCheckpoint(
        model_name,
        monitor='val_accuracy',
        save_best_only=True,
        save_weights_only=False,
        mode='max',
        verbose=0
    )

def callback_earlystop(patience):
    return tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=patience,
        mode='max'
    )