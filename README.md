Autism Detection using AI

🚀 Overview

This project is an AI-powered autism detection system that analyzes eye and facial patterns using deep learning to identify early signs of autism.

👉 Built using transfer learning, the system enables:

Real-time predictions
Scalable deployment
AI-driven healthcare support

🎯 Objective

Early autism detection
Reduce manual diagnosis effort
Enable real-time screening
Build an end-to-end AI pipeline

🧾 Dataset

Source: Kaggle
Type: Image dataset (eye behavior)

📁 Structure

ASDeyedata/
 ├── TSImages-1   → Autism
 ├── TCImages-0   → Non-Autism
⚙️ Preprocessed Data
data/
 ├── train/
 │    ├── autism/
 │    └── non_autism/
 ├── test/
 │    ├── autism/
 │    └── non_autism/

🧠 Model Architecture
🔹 Base Model
InceptionV3 (Transfer Learning)
🔹 Custom Layers
Global Average Pooling
Dense (128, ReLU)
Dropout (0.5)
Output (Sigmoid)

🏗️ System Architecture

📊 Diagram (Mermaid — GitHub Supported)

<img width="531" height="1542" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/5630673d-885f-44c0-ae44-d373fd2f5fd9" />

🖼️ Visual Architecture (For Judges)
        ┌──────────────┐
        │   Frontend   │ (React)
        └──────┬───────┘
               │ Image Upload
               ▼
        ┌──────────────┐
        │   Backend    │ (Flask API)
        └──────┬───────┘
               │ Preprocessing
               ▼
        ┌──────────────┐
        │   AI Model   │ (.h5 - InceptionV3)
        └──────┬───────┘
               │ Prediction
               ▼
        ┌──────────────┐
        │   Response   │ (JSON)
        └──────────────┘

⚙️ Training Details
Parameter	Value
Input Size	224×224
Batch Size	32
Optimizer	Adam
Loss	Binary Crossentropy
Epochs	10–15
Callback	EarlyStopping

📊 Performance
✅ Test Accuracy

84%

📈 Classification Metrics
Precision
Recall
F1-score

🔍 Key Insight
Strong Non-Autism detection
Slightly lower Autism recall → improvement scope

📊 Confusion Matrix
           Predicted
          0        1
Actual  ----------------
0      |  TP     FP |
1      |  FN     TP |

👉 Focus: Reduce False Negatives (Autism missed cases)

⚠️ Challenges

Small dataset
Overfitting
Class imbalance

🚀 Improvements Applied

Data Augmentation
Dropout Regularization
EarlyStopping
Transfer Learning

🔮 Future Scope

Improve Autism Recall
Add real-time webcam detection
Deploy on edge devices (Jetson)
Use advanced models (CNN + LSTM)

🖥️ Backend (Flask API)

▶️ Run Backend

pip install -r requirements.txt
python app.py

🔗 API Endpoint

POST /predict

🌐 Frontend Integration

const sendImage = async (file) => {
  const formData = new FormData();
  formData.append("image", file);

  const response = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    body: formData
  });

  const data = await response.json();
  console.log(data);
};

📦 Dependencies

TensorFlow
OpenCV
Flask
NumPy

💡 Key Features

✅ Real-time prediction
✅ End-to-end pipeline
✅ Scalable backend
✅ AI healthcare application

This project demonstrates how AI can assist early diagnosis in healthcare, making screening faster, accessible, and scalable.

👩‍💻 Contributors

Adriza Srivastava
Nandini Singh
Aastha Singh
