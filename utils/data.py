import pathlib, keras

# loading the dataset
def load_split_datasets(base_dir, image_size = (224, 224), batch_size = 64):
    if not pathlib.Path(base_dir).exists():
        raise ValueError(f"Directory {base_dir} does not exist")

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

def load_unified_datasets(base_dir, image_size = (224, 224), batch_size = 64):
    if not pathlib.Path(base_dir).exists():
        raise ValueError(f"Directory {base_dir} does not exist")
        
    train_dataset = keras.utils.image_dataset_from_directory(
        pathlib.Path(base_dir),
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=image_size,
        batch_size=batch_size,
        label_mode='categorical'
    )

    val_test_dataset = keras.utils.image_dataset_from_directory(
        pathlib.Path(base_dir),
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=image_size,
        batch_size=batch_size,
        label_mode='categorical'
    )

    # Split validation dataset into validation and test sets
    val_batches = len(val_test_dataset) // 2
    val_dataset = val_test_dataset.take(val_batches)
    test_dataset = val_test_dataset.skip(val_batches)
    
    return train_dataset, val_dataset, test_dataset