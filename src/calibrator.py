# calibrator.py — mô-đun hiệu chỉnh cơ bản (tạm thời bỏ qua, chỉ trả về identity)
class Calibrator:
    def __init__(self):
        self.enabled = False

    def calibrate(self):
        print("Calibration skipped (default mapping used).")

    def map_coords(self, x, y):
        return x, y
