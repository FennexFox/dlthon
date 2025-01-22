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

async def predict(model, img):
    try:
        # 파일 포인터 리셋
        await img.seek(0)
        
        # 이미지 읽기 및 검증
        contents = await img.read()
        if not contents:
            raise ValueError("Empty image file")
        
        # 디버깅을 위한 파일 크기 출력
        print(f"File size: {len(contents)} bytes")
            
        image_bytes = io.BytesIO(contents)
        image_bytes.seek(0)  # 파일 포인터 리셋
        
        # 이미지 형식 검증 후 열기
        try:
            pil_image = Image.open(image_bytes)
            pil_image.verify()  # 이미지 파일 검증
            image_bytes.seek(0)  # 검증 후 포인터 리셋
            pil_image = Image.open(image_bytes)  # 다시 열기
        except Exception as e:
            raise ValueError(f"Invalid image format: {e}")
        
        # PIL Image로 로드 및 크기 조정
        pil_image = pil_image.resize((224, 224))
        
        # numpy 배열로 변환 및 전처리
        img_array = keras.utils.img_to_array(pil_image)
        img_array = tf.expand_dims(img_array, 0)  # 배치 차원 추가
        
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        return {
            "class": class_names[np.argmax(score)-1],
            "score": float(100 * np.max(score))  # numpy float을 Python float으로 변환
        }
    except Exception as e:
        raise Exception(f"failed to predict: {e}")