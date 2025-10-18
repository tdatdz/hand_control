# utils.py — hàm tiện ích
import numpy as np
import cv2

def smooth(prev, new, alpha=0.7):
    return alpha * prev + (1 - alpha) * new

def draw_text(img, text, pos=(10, 30), color=(0, 255, 0)):
    cv2.putText(img, text, pos, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

def calc_distance(p1, p2):
    return np.hypot(p1[0] - p2[0], p1[1] - p2[1])
