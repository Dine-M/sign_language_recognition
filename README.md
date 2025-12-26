# sign_language_recognition using yolov7

📌 Project Overview:

Sign Language Recognition is an important assistive technology that helps bridge the communication gap between hearing-impaired individuals and the rest of society.
This project implements a real-time sign language recognition system using YOLOv7, a high-performance object detection model.
The system detects hand gestures from live video input and classifies them into predefined sign labels with fast and accurate real-time performance.

🎯 Objectives

• Detect hand gestures in real time using a webcam
• Train a deep learning model on a custom sign language dataset
• Achieve high accuracy with low inference latency
• Build a clean, modular, and extensible recognition pipeline

🚀 Features

• Real-time webcam-based detection
• YOLOv7-powered object detection
• Custom dataset training support
• Clean and GitHub-friendly project structure
• Google Colab compatible training setup

🛠️ Tech Stack

• Programming Language: Python
• Deep Learning Framework: PyTorch
• Model: YOLOv7
• Computer Vision: OpenCV
• Training Environment: Google Colab / Local Machine
• Version Control: Git & GitHub

📂 Project Structure

sign-language-recognition/

│

├── README.md

├── requirements.txt

├── .gitignore
│

├── data/
│   └── custom.yaml
│
├── scripts/
│   ├── train_model.py
│   └── detect_realtime.py
│
└── notebooks/
    └── training_colab.ipynb
    
📊 Dataset Details

• Custom sign language gesture dataset
• Images annotated in YOLO format
• Dataset split into training and validation sets

Dataset Configuration (data/custom.yaml)
(code)
train: data/images/train
val: data/images/val

nc: 1
names: ['sign']
⚠️ Dataset images and labels are not included in this repository due to size constraints.

⚙️ Setup & Installation
1️⃣ Clone YOLOv7 Repository
(Code)
git clone https://github.com/WongKinYiu/yolov7
2️⃣ Install Dependencies
(Code)
pip install -r requirements.txt
3️⃣ Download Pretrained Weights
Download yolov7.pt from the official YOLOv7 releases and place it in the project root or YOLOv7 directory.

🏋️ Model Training
Run the training script:
(Code)python scripts/train_model.py
Trained model weights will be saved automatically in:
(Code)runs/train/exp/weights/

🎥 Real-Time Detection
To start live sign language recognition using a webcam:
(code)python scripts/detect_realtime.py

📈 Results
• Accurate gesture detection on trained sign classes
• Smooth real-time inference
• Efficient performance using YOLOv7 architecture
(Performance depends on dataset quality and hardware configuration)
  
🧩 Applications
• Assistive communication systems
• Educational tools for hearing-impaired learners
• Human–computer interaction
• Gesture-based control systems

🔮 Future Enhancements
• Sentence-level sign language recognition
• Gesture-to-speech conversion
• Mobile or web-based deployment
• Support for multiple sign languages

⚠️ Important Note
• This project uses the official YOLOv7 implementation.
• The primary contributions of this project include:
• Dataset preparation and annotation
• Model training and fine-tuning
• Real-time inference pipeline
• Project integration and documentation

👨‍💻 Team Members
• Dinesh Kumar M
• Dileep Adhithyan K
• Aathavan S K

📜 License
This project is intended for academic and educational purposes only.

⭐ Acknowledgements
• YOLOv7 by WongKinYiu
• PyTorch Community
• OpenCV Contributors



