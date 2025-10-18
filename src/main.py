# main.py — khởi chạy toàn bộ hệ thống
import cv2
import pyautogui
from hand_detector import HandDetector
from gesture_recognizer import GestureRecognizer
from cursor_controller import CursorController
from calibrator import Calibrator
import config

def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    gesture = GestureRecognizer(config.PINCH_THRESHOLD, config.CLICK_COOLDOWN)
    controller = CursorController(pyautogui.size(), config.SMOOTHING_ALPHA)
    calib = Calibrator()
    calib.calibrate()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        landmarks, frame = detector.detect(frame, draw=config.SHOW_LANDMARKS)
        if landmarks:
            x, y = landmarks[0][8][0], landmarks[0][8][1]
            x, y = calib.map_coords(x, y)
            controller.move(x, y)

            g = gesture.recognize(landmarks)
            if g == "CLICK_DOWN":
                controller.click_down()
            elif g == "CLICK_UP":
                controller.click_up()

        cv2.imshow("Hand Control", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC để thoát
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
