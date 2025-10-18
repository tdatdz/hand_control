from src.gesture_recognizer import GestureRecognizer
import time

def test_gesture_recognizer():
    gesture = GestureRecognizer(threshold=0.05, cooldown=0.2)
    fake_landmarks = [[(0,0,0)]*21]
    fake_landmarks[0][8] = (0.5, 0.5, 0)  # index
    fake_landmarks[0][4] = (0.52, 0.5, 0) # thumb gần nhau

    print(gesture.recognize(fake_landmarks))  # CLICK_DOWN
    time.sleep(0.3)
    fake_landmarks[0][4] = (0.9, 0.9, 0)     # tách ra
    print(gesture.recognize(fake_landmarks))  # CLICK_UP

if __name__ == "__main__":
    test_gesture_recognizer()
