import cv2 as cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array

face_prototxtPath = "deploy.prototxt"
face_weightsPath = "res10_300x300_ssd_iter_140000.caffemodel"
age_prototxtPath = "deploy_age.prototxt"
age_weightsPath = "age_net.caffemodel"
faceNet = cv2.dnn.readNet(face_prototxtPath, face_weightsPath)
ageNet = cv2.dnn.readNet(age_weightsPath, age_prototxtPath)

AGE_BUCKETS = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(25-32)",
               "(38-43)", "(48-53)", "(60-100)"]


def send_email():
    return None


def get_faces(frame):
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),
                                 (104.0, 117.0, 123.0))

    faceNet.setInput(blob)
    detections = faceNet.forward()

    faces = []
    ages = []
    locations = []

    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

            face = frame[startY:endY, startX:endX]

            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (224, 224))
            face = img_to_array(face)
            face = preprocess_input(face)

            faces.append(face)
            locations.append((startX, startY, endX, endY))
    return faces, locations


def get_ages(frame, locations):
    ages = []
    for location in locations:
        (startX, startY, endX, endY) = location
        face = frame[startY:endY, startX:endX]
        face_blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227),
                                      (104.0, 117.0, 123.0))
        ageNet.setInput(face_blob)
        preds = ageNet.forward()
        index = preds[0].argmax()
        age = AGE_BUCKETS[index]
        # age_confidence = preds[0][index]
        ages.append(age)
    return ages


def get_camera_capture():
    cap = cv2.VideoCapture(0)
    while not cap.isOpened():
        cap = cv2.VideoCapture(0)
    return cap


def process_the_ages(ages):
    return None


def controller(vid, file):
    return_ages = []
    if not vid.isOpened():
        vid = get_camera_capture()
    # Capture the video frame
    # by frame
    else:
        ret, frame = vid.read()
        frame = cv2.flip(frame, 1)

        faces, locations = get_faces(frame)
        ages = get_ages(frame, locations)
        counter = 0
        for box in locations:
            (startX, startY, endX, endY) = box
            age = ages[counter]
            return_ages = ages
            label = "the age is: " + str(age)
            cv2.putText(frame, label, (startX, startY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
            cv2.rectangle(frame, (startX - 10, startY - 10), (endX + 10, endY + 10), (0, 255, 0), 2)
            counter += 1
        # Display the resulting frame
        # cv2.imshow('frame', frame)
        cv2.imwrite(file, frame)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice

        # After the loop release the cap object
    vid.release()
    return return_ages


if __name__ == "__main__":
    baby_vid = cv2.VideoCapture(0)
    driver_vid = cv2.VideoCapture(1)
    baby_file = 'baby.jpg'
    driver_file = 'driver.jpg'

    while True:
        controller(baby_vid, baby_file)
        controller(driver_vid, driver_file)
        if cv2.waitKey(10000) & 0xFF == ord('q'):
            break




