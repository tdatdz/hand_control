from src.cursor_controller import CursorController
import pyautogui
import time

def test_cursor_controller():
    controller = CursorController(pyautogui.size(), alpha=0.7)
    print("Di chuyển con trỏ trong 3s...")
    for i in range(100):
        x = i / 100
        y = i / 100
        controller.move(x, y)
        time.sleep(0.02)
    print("Thử click...")
    controller.click_down()
    time.sleep(0.2)
    controller.click_up()
    print("Xong!")

if __name__ == "__main__":
    test_cursor_controller()
