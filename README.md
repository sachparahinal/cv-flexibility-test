# Chair Sit-and-Reach Flexibility Test (Computer-Vision Guided)

A webcam-based seated flexibility assessment tool built on the **Rikli & Jones Senior Fitness Test** protocol. Uses MediaPipe pose detection and OpenCV to guide users through a standardized flexibility test and automatically measure reach distance — no physical equipment required.

Developed by **Hinal Sachpara** - Machine Learning Intern, MyEdMaster LLC, Spring 2026.

---

## Features

- **Before You Begin Screen** - 7-point pre-test checklist for environment and camera setup
- **Sitting Check** - detects seated position using hip-to-knee Y ratio (threshold 0.88, side-view camera)
- **Leg Extended Check** - validates straight leg using 3D hip-knee-ankle angle (threshold 155°)
- **Foot Flat Check** - confirms one foot flat on floor via heel-toe Y alignment (tolerance 0.06)
- **Hands Position Check** - verifies stacked hand position per Rikli & Jones protocol
- **Inhale Preparation** - cues participant to inhale before reaching
- **Forward Reach** - tracks reaching motion toward toes using horizontal X alignment
- **Hold Position** - enforces 2-second hold before measurement
- **Flexibility Measurement** - computes 3D reach distance and classifies result
- **Result Screen** - animated result card with category and motivational message
- **Timer Pause/Resume** - 2-chances rule, timer pauses on position break, restarts on 3rd break
- **Dark Room Detection** - dedicated error message when lighting is insufficient
- **Audio Guidance** - MP3-based TTS system with countdown and instruction audio
- **Fullscreen Display** - fullscreen OpenCV window with branded color scheme

---

## Result Categories (Rikli & Jones Protocol)

| Category | Criteria |
|---|---|
| Above Average | Fingertips past toes by more than 4 inches |
| Average | Fingertips within 4 inches either side of toes |
| Below Average | Fingertips more than 4 inches short of toes |

---

## Tech Stack

- **Pose Detection:** MediaPipe BlazePose (min_detection_confidence: 0.6)
- **Computer Vision:** OpenCV
- **Numerical Processing:** NumPy
- **Audio:** FullMP3TTS — custom MP3-based cross-platform TTS
- **Environment:** Python 3.12, Jupyter Notebook
- **Platform:** macOS (fullscreen via cv2.WND_PROP_FULLSCREEN)

---

## Requirements

- Python 3.12
- Webcam (USB or built-in)

### Install dependencies:

```bash
pip install mediapipe opencv-python numpy
```

---

## How To Run

1. Open `chair_sit_and_reach_final_working_Hinal.ipynb` in Jupyter Notebook
2. Run all cells in order: **STEP 1 → STEP 18**
3. Position your camera **to your side at hip height**
4. Stand fully in the camera frame during pre-countdown
5. Follow the on-screen and audio instructions

---

## Camera Setup

The test requires a **side-view camera** at hip height. This is essential for:
- Accurate leg extension angle calculation
- Reliable reach distance measurement
- Correct sitting position detection

---

## Project Structure

```
cv-flexibility-test-main/
├── chair_sit_and_reach_final_working_Hinal.ipynb   # Main notebook
├── tts_final.py                                     # TTS audio system
├── visual_instruction.png                           # Visual instruction image
├── audio/                                           # MP3 audio files
├── CHANGELOG.md                                     # Full development history
└── README.md
```

---

## Test Flow

```
Instruction Screens (Before You Begin → Test Steps → Visual Guide)
        ↓
Pre-Countdown (full body detection)
        ↓
Countdown 3-2-1-GO
        ↓
Sitting → Leg Extended → Foot Flat → Hands → Inhale → Reach → Hold → Measurement
        ↓
Result Screen
```
