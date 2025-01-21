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

def load_unified_datasets(base_dir, image_size = (224, 224), batch_size = 64, val_split = 0.4):
    if not pathlib.Path(base_dir).exists():
        raise ValueError(f"Directory {base_dir} does not exist")
        
    dataset = keras.utils.image_dataset_from_directory(
        pathlib.Path(base_dir),
        validation_split=val_split,
        subset="both",
        seed=123,
        image_size=image_size,
        batch_size=batch_size,
        label_mode='categorical'
    )
    
    train_dataset = dataset[0]

    # Split validation dataset into validation and test sets
    val_batches = len(dataset[1]) // 2
    val_dataset = dataset[1].take(val_batches)
    test_dataset = dataset[1].skip(val_batches)
    
    return train_dataset, val_dataset, test_dataset