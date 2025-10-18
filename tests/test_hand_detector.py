from src.hand_detector import HandDetector
import cv2

def test_hand_detector():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    print("Press Esc to exit")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        landmarks, frame = detector.detect(frame)
        if landmarks:
            print("Phát hiện tay:", len(landmarks[0]), "landmarks")
        cv2.imshow("test_hand_detector", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_hand_detector()
