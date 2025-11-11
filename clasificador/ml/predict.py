import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

CLASSES = [
    'Carton',
    'Vidrio',
    'Metal',
    'Organico',
    'Papel',
    'Plastico',
    'Basura'
]

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'modelo_clasificador.h5')
MODEL = tf.keras.models.load_model(MODEL_PATH)

def predict_image(img_path):
    """Recibe una ruta de imagen y retorna la clase predicha"""
    img = image.load_img(img_path, target_size=(224, 224))  
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    predictions = MODEL.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    return CLASSES[predicted_class]