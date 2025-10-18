# hand_detector.py — phát hiện và trích xuất keypoints bàn tay bằng MediaPipe
import mediapipe as mp
import cv2

class HandDetector:
    def __init__(self, max_hands=1, det_conf=0.6, track_conf=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
            min_detection_confidence=det_conf,
            min_tracking_confidence=track_conf
        )
        self.mp_draw = mp.solutions.drawing_utils

    def detect(self, frame, draw=True):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)
        landmarks = []

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                single = []
                for lm in handLms.landmark:
                    single.append((lm.x, lm.y, lm.z))
                landmarks.append(single)
                if draw:
                    self.mp_draw.draw_landmarks(frame, handLms, self.mp_hands.HAND_CONNECTIONS)
        return landmarks, frame
