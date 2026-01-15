# cv-flexibility-test
Computer-Vision Guided Chair Sit-and-Reach Test

# Chair Sit-and-Reach Flexibility Test (Computer-Vision Guided)

This project implements a **computer-vision guided Chair Sit-and-Reach flexibility test** using **MediaPipe Pose** and **OpenCV**.  
It automates the process of posture validation, reach measurement, and session guidance without the need for manual supervision.  

---

## 📌 Features
- **Sitting Check** – verifies seated posture using hip–knee vertical alignment  
- **Foot Flat Check** – ensures one foot is flat (heel vs. toe Y-alignment)  
- **Leg Extended Check** – detects if one leg is fully straight (3D hip-knee-ankle angle)  
- **Hands Position Check** – confirms one hand placed over the other  
- **Inhale Preparation** – cues the participant to inhale before reaching  
- **Forward Reach** – tracks reaching motion toward toes  
- **Hold Position** – enforces holding stretch for ≥2 seconds  
- **Measurement** – computes reach distance (currently placeholder logic)  
- **Complete** – displays final result  

---

## 🏗️ Tech Stack
- **ML Model**: MediaPipe Pose (BlazePose)  
- **Libraries**:  
  - [MediaPipe](https://developers.google.com/mediapipe/) – landmark detection  
  - [OpenCV](https://opencv.org/) – video capture, drawing, UI  
  - [NumPy](https://numpy.org/) – math utilities  
  - Python standard libs: `math`, `time`, `enum`  

---

## 📂 Planned Features
- OpenCV-based **video recording** of test sessions (for replay & validation)  
- Database integration for storing historical flexibility test results  

---

## ⚙️ Requirements
- Python **3.12**  
- Webcam (USB or inbuilt)  

### Install dependencies:
```bash
pip install mediapipe opencv-python opencv-contrib-python numpy matplotlib
