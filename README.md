# 🛵 Helmet Detection using YOLOv8 🚀

This project uses YOLOv8 to detect whether a person is wearing a helmet on a two-wheeler. It includes two main phases:

1. 🧠 **Model Training** using a custom dataset with YOLOv8 on Google Colab.
2. 🌐 **Web Application** built using Flask to allow users to upload images and get real-time helmet detection.

---

## 📁 Project Structure

ProjectHelmetDetection/
│
├── training/
│   └── HelmetDetection.v1i.yolov8.zip/
|       ├── train/ 
|       ├── valid/
|       └── data.yaml
│
│
├── webApp/                                     # Web application for helmet detection
│   ├── best.pt                                 # YOLOv8 trained model downloaded from Colab
│   ├── app.py                                  # Flask backend (or main backend logic)
│   ├── static/                                 # Static assets like CSS, JS
│   │   ├── results
│   │   └── uploads
│   └── templates/
│       ├── index.html         # HTML templates
|
├── README.md
---

## 📌 PHASE 1: Model Training on Google Colab

### ✅ Steps Followed:

1. **Prepared Custom Dataset**:
    - Used images and PASCAL VOC XML annotations.
    - Exported dataset in YOLOv8 format via Roboflow.
    - Folder structure:
      ```
      HelmetDetection.v1i.yolov8/
      ├── train/
      ├── valid/
      └── data.yaml
      ```

2. **Compressed** into `HelmetDetection.v1i.yolov8.zip` and uploaded to Colab.

3. **Installed Ultralytics Library**:
    ```python
    !pip install ultralytics
    from ultralytics import YOLO
    ```

4. **Unzipped and Verified Dataset**:
    ```python
    !unzip HelmetDetection.v1i.yolov8.zip -d /content/
    ```

5. **Trained the Model**:
    ```python
    model = YOLO("yolov8m.pt")
    model.train(
        data="/content/HelmetDetection.v1i.yolov8/data.yaml",
        epochs=100,
        patience=10,
        imgsz=640,
        batch=16,
        project="yolov8_model",
        name="helmet_detection_v2",
        verbose=True
    )
    ```

6. **Training Completed with Early Stopping** at Epoch 36 (Best at 26).

7. **Downloaded Trained Weights**:
    ```python
    from google.colab import files
    files.download('/content/yolov8_model/helmet_detection_v2/weights/best.pt')
    ```

---

## 🌐 PHASE 2: Helmet Detection Web Application

### 🚀 Tech Stack

- Frontend: `HTML`, `CSS`, JavaScript (for animations)
- Backend: `Flask`
- AI Model: `YOLOv8` using `ultralytics` Python package

### ✅ Features

- Upload any image containing people on two-wheelers.
- Detect helmets with high accuracy.
- Display output image with bounding boxes and confidence scores.
- Beautiful and responsive UI.

### 🧾 How to Run the Web App

1. Place your `best.pt` model file in:
    ```
    webApp/best.pt
    ```

2. Run the Flask App:
    ```bash
    cd HelmetDetectionWebApp
    python app.py
    ```

3. Open in Browser:
    ```
    http://localhost:5000
    ```

4. Upload an image and view results.

---

## 📸 Sample Output

![Helmet Detection](static/result.jpg)

---

## 📚 Requirements

- Python 3.7+
- Flask
- Ultralytics YOLOv8

Install dependencies:
```bash
pip install flask ultralytics


✨ Future Improvements
Add support for video stream input.

Deploy the web app on cloud (Heroku, Render, or AWS).

Integrate real-time camera detection.

👤 Author
Ayush Sirswal

BCA Final Year

YOLOv8 | AI-Powered Safety Projects

