import tensorflow, keras

def callback_savemodel(model_name, monitor='val_loss'):
    return keras.callbacks.ModelCheckpoint(
        model_name,
        monitor=monitor,
        save_best_only=True,
        save_weights_only=False,
        verbose=0
    )

def callback_earlystop(patience, monitor='val_loss'):
    return keras.callbacks.EarlyStopping(
        monitor=monitor,
        patience=patience,
    )