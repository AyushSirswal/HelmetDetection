from flask import Flask, request, send_file
from ultralytics import YOLO
import os
import uuid
from PIL import Image
import shutil

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['RESULT_FOLDER'] = 'static/results'

# Load trained model
model = YOLO("best.pt")

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return open('templates/index.html').read()

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No image provided", 400

    file = request.files['image']
    if file.filename == '':
        return "Empty filename", 400

    # Save uploaded image
    filename = f"{uuid.uuid4()}.jpg"
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(upload_path)

    # Run prediction
    results = model.predict(upload_path, save=True, save_txt=False, conf=0.3)
    
    # Extract result image path
    result_dir = results[0].save_dir
    result_img_path = os.path.join(result_dir, os.path.basename(upload_path))

    # Save final image to results folder
    final_result_path = os.path.join(app.config['RESULT_FOLDER'], f"result_{filename}")
    img = Image.open(result_img_path)
    img.save(final_result_path)

    # Clean up prediction folder
    shutil.rmtree(result_dir, ignore_errors=True)

    return send_file(final_result_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
