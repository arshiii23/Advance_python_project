📷 Face Detection System (OpenCV Project)

🚀 Overview

The Face Detection System is a real-time computer vision project built using Python and OpenCV. The application uses a webcam to detect human faces and draw rectangles around them in real time.

This project demonstrates practical concepts of:

- Computer Vision
- Real-time video processing
- Face detection using Haar Cascades
- OpenCV integration

It is a great beginner-to-intermediate AI project for portfolios and GitHub.

---

🧠 Features

- Real-time webcam face detection
- Detects multiple faces simultaneously
- Draws rectangles around detected faces
- Uses OpenCV Haar Cascade classifier
- Simple and beginner-friendly implementation

---

🛠️ Technologies Used

- Python
- OpenCV
---

⚙️ Installation & Setup

1. Clone the repository or download files

---

2. Install required library

pip install opencv-python

---

3. Run the project

python main.py

---

💻 Complete Code ("main.py")

import cv2

# Load face detection classifier
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Start webcam
cap = cv2.VideoCapture(0)

while True:

    # Read webcam frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4
    )

    # Draw rectangles around faces
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

    # Show webcam output
    cv2.imshow("Face Detection System", frame)

    # Press Q to quit
    if cv2.waitKey(1) == ord("q"):
        break

# Release webcam
cap.release()

# Close all windows
cv2.destroyAllWindows()

---

▶️ How It Works

1. OpenCV accesses the webcam
2. Video frames are captured continuously
3. Frames are converted to grayscale
4. Haar Cascade classifier detects faces
5. Rectangles are drawn around detected faces
6. Webcam feed is displayed in real time

---

💻 Example Output

Real-time webcam window opens
Faces are highlighted with blue rectangles
Press Q to exit

---

🎯 Skills Demonstrated

- Computer Vision
- OpenCV Integration
- Real-time Video Processing
- Face Detection Algorithms
- Python Application Development

---

🔮 Future Improvements

- Add face recognition
- Add eye and smile detection
- Save detected faces automatically
- Build attendance system using face recognition
- Create GUI version using Tkinter or Streamlit

---

👨‍💻 Author

Arsheen Shaikh

---
