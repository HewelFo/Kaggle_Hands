import mediapipe as mp
import cv2
import numpy as np
import uuid
import os


mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


captu = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.9, min_tracking_confidence=0.5) as hands:
    while captu.isOpened():
        ret, frame = captu.read()

        # BGR -> RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)

        image.flags.writeable = False

        result = hands.process(image)

        image.flags.writeable = True

        # RGB -> BGR
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        print(result)
        # para ver los puntos de las manos en en x, y, z
        # result.multi_hand_landmarks
        # muestra a que parte representa cada punto
        # mp_hands.HAND_CONNECTIONS


        if result.multi_hand_landmarks:
            for num, hand in enumerate(result.multi_hand_landmarks):
                mp_draw.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)



        cv2.imshow('hand detection', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

captu.release()
cv2.destroyAllWindows()