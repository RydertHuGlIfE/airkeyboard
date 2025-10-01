# Virtual Hand Gesture Keyboard 🖐️⌨️

This project implements a **virtual keyboard** controlled entirely by **hand gestures** using **OpenCV**, **cvzone**, and **pynput**.  
You can press keys by hovering your index finger over them and "tapping" with your thumb (detected via fingertip distance).

---

## 🚀 Features
- Virtual on-screen keyboard with multiple rows of keys (`Q → /`).
- Hand detection powered by [cvzone HandTrackingModule](https://github.com/cvzone/cvzone).
- Real-time fingertip tracking using **OpenCV**.
- Press keys by pinching index finger and thumb together.
- Typed characters appear live on screen.
- Keys are also sent to your system keyboard using **pynput**.

---

## 📂 Project Structure
# airkeyboard



---

## 🔧 Requirements
Install the required dependencies:

```bash
pip install opencv-python cvzone pynput
```


Works best with python3.10

Customize Layout 

keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
]



Change size: def __init__(self, pos, text, size=[85, 85]):



Tap Senstivity: if l < 35:  # decrease or increase
