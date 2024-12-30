import tensorflow as tf
from tensorflow.keras.models import load_model

import numpy
from tensorflow.keras.preprocessing import image

# Load the pre-trained model
model = load_model('Models/StrokeClassifier.keras')

# Function to preprocess input data
def preprocess_input(data):
    # Assuming data is a numpy array
    # Normalize or preprocess data as required by your model
    return data / 255.0

# Function to analyze input data using the model
def analyze_data(data):
    preprocessed_data = preprocess_input(data)
    predictions = model.predict(preprocessed_data)
    return predictions

# Example usage
# Load and preprocess the image
img_path = 'Dataset/Validate/noStroke_data/aug_0_8545.jpg'  # Replace with the actual image path
img = image.load_img(img_path, target_size=(32, 32))  # Adjust target_size as required by your model
input_data = image.img_to_array(img)
input_data = numpy.expand_dims(input_data, axis=0)

# Analyze the image data
analysis_result = analyze_data(input_data)
print(analysis_result)