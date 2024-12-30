import numpy as np
import io
import os
import tensorflow as tf
from flask import Flask, request, jsonify
from PIL import Image
from tensorflow.keras.models import load_model
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

# Path to the trained model
MODEL_PATH = './StrokeClassifier.keras'
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

# Load the trained CNN model
def load_cnn_model():
    return load_model(MODEL_PATH)

model = load_cnn_model()

@app.route('/predict', methods=['POST'])
def predict_stroke():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    try:
        # Process the image file
        image = Image.open(io.BytesIO(file.read())).convert("RGB")  # Ensure the image is in RGB format
        image = image.resize((256, 256))  # Resize the image to the model's expected input size
        image_array = np.array(image) / 255.0  # Normalize pixel values
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension (1, 256, 256, 3)

        # Make a prediction
        prediction = model.predict(image_array)
        stroke_probability = float(prediction[0][0])  # Extract the probability

        return jsonify({
            'probability': stroke_probability,
            'has_stroke': stroke_probability > 0.5  # Threshold for stroke prediction
        })
    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
