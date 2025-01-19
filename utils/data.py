import pathlib, keras

# loading the dataset
def load_datasets(base_dir, image_size = (224, 224), batch_size = 64):
    base_dir = pathlib.Path(f'{base_dir}/Train_Test_Valid')

    train_dataset = keras.utils.image_dataset_from_directory(
        base_dir / "train",
        image_size = image_size,
        batch_size = batch_size,
        label_mode='categorical')

    val_dataset = keras.utils.image_dataset_from_directory(
        base_dir / "valid",
        image_size = image_size,
        batch_size = batch_size,
        label_mode='categorical')

    test_dataset = keras.utils.image_dataset_from_directory(
        base_dir / "test",
        image_size = image_size,
        batch_size = batch_size,
        label_mode='categorical')
    
    return train_dataset, val_dataset, test_dataset