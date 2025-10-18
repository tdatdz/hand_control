# cursor_controller.py — điều khiển chuột dựa trên cử chỉ
import pyautogui
from utils import smooth

class CursorController:
    def __init__(self, screen_size, alpha=0.7):
        self.screen_w, self.screen_h = screen_size
        self.smooth_x, self.smooth_y = 0, 0
        self.alpha = alpha

    def move(self, norm_x, norm_y):
        x = self.screen_w - norm_x * self.screen_w
        y = norm_y * self.screen_h
        self.smooth_x = smooth(self.smooth_x, x, self.alpha)
        self.smooth_y = smooth(self.smooth_y, y, self.alpha)
        pyautogui.moveTo(self.smooth_x, self.smooth_y)

    def click_down(self):
        pyautogui.mouseDown()

    def click_up(self):
        pyautogui.mouseUp()
