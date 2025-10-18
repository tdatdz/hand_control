# gesture_recognizer.py — nhận diện cử chỉ cơ bản
import time
from utils import calc_distance

class GestureRecognizer:
    def __init__(self, threshold, cooldown):
        self.threshold = threshold
        self.cooldown = cooldown
        self.last_click_time = 0
        self.pinch_down = False

    def recognize(self, landmarks):
        if not landmarks:
            return None

        # lấy bàn tay đầu tiên
        lm = landmarks[0]
        ix, iy = lm[8][0], lm[8][1]   # index tip
        tx, ty = lm[4][0], lm[4][1]   # thumb tip
        dist = calc_distance((ix, iy), (tx, ty))
        now = time.time()

        gesture = None
        if dist < self.threshold and not self.pinch_down and now - self.last_click_time > self.cooldown:
            self.pinch_down = True
            self.last_click_time = now
            gesture = "CLICK_DOWN"
        elif dist >= self.threshold and self.pinch_down:
            self.pinch_down = False
            gesture = "CLICK_UP"

        return gesture
