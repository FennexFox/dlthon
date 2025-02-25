import os, io
import keras, tensorflow as tf, numpy as np
from PIL import Image

class_names = ['Barrel', 'Blue', 'Compass', 'Lions', 'Mauve', "Moon"]

def load_model(model_name = 'eV2L_midsize3.keras'):
    model_path = os.path.expanduser(f'~/keras/dlthon/{model_name}')

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    model = keras.models.load_model(model_path)
    
    print(model.summary())
    
    return model

def predict(model, img):
    try:
        # PIL Image 검증
        if not isinstance(img, Image.Image):
            raise ValueError("Input must be a PIL Image object")
        
        # 이미지 크기 조정
        img = img.resize((224, 224))
        
        # numpy 배열로 변환 및 전처리
        img_array = keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # 배치 차원 추가
        
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        return {
            "species": class_names[np.argmax(score)-1],
            "description": "it's not a description",
            "confidence": float(np.max(score))
        }
    except Exception as e:
        raise Exception(f"Prediction failed: {str(e)}")