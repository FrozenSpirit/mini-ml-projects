# Write a Python Script that captures images from your webcam video stream
# Extracts all Faces from the image frame (using haarcascades)
# Stores the Face information into numpy arrays
#
# Steps
# 1. Read and show video stream, caputre images
# 2. Detect Faces and show bounding box
# 3. Flatten the largest face image and save(gray_img) in a numpy array
# 4. Repeat the above for multiple people to generate training data

import cv2
import numpy

# Initialize Camera
cap = cv2.VideoCapture(0)

# Face Detection
face_cascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

skip = 0
face_data = []

while True:
    success, frame = cap.read()

    # due to any problem couldn't take image
    if not success:
        continue

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    # faces returns (x, y, w, h), area = w * h, so
    faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)

    # pick the largest face, we getting that by sorting it all
    for face in faces[-1:]:
        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # cropping out the required face : Region of Interest
        offset = 10  # its the padding we give around cropped image
        face_section = frame[y - offset: y + h + offset, x - offset: x + w + offset]
        # each image is a matrix so we can slice, here height comes first

        # resizing the image to our requirement
        face_section = cv2.resize(face_section, (100, 100))

        # capturing every 10th face
        skip += 1
        if skip % 10 == 0:
            face_data.append(face_section)
            print(len(face_data))

        cv2.imshow("Frame Section", face_section)

    cv2.imshow("Frame", frame)

    # waitKey(1) returns 32 bit and 0xFF gives 8 binary, if 113 (val of ord(q)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
