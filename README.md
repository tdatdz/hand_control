## 🖐️ Hand Control – Gesture Based Controller
## 📌 Giới thiệu

Hand Control là dự án cho phép nhận diện và điều khiển máy tính hoặc thiết bị bên ngoài bằng cử chỉ tay thông qua camera.
Chương trình sử dụng Computer Vision và Machine Learning (MediaPipe) để phát hiện bàn tay, nhận dạng các điểm mốc (landmarks), và thực hiện hành động tương ứng như:

- Di chuyển chuột

- Click chuột

- Điều khiển âm lượng / đèn LED / robot tay qua cổng Serial

## 🚀 Tính năng chính

 ✅ Nhận diện bàn tay và các ngón tay theo thời gian thực                      
 ✅ Xác định toạ độ và cử chỉ tay (giơ 1 ngón, 2 ngón, nắm đấm, v.v.)            
 ✅ Giao tiếp với máy tính hoặc thiết bị Arduino qua Serial hoặc PyAutoGUI              
 ✅ Có thể mở rộng cho các ứng dụng:

- Điều khiển con trỏ chuột

- Điều khiển robot arm

- Giao diện cảm ứng ảo

- Game điều khiển bằng tay

## 🧠 Công nghệ sử dụng
```
Thành phần	Mô tả
Python 3.x	Ngôn ngữ chính
OpenCV	Xử lý hình ảnh và đọc video từ camera
MediaPipe Hands	Nhận diện bàn tay, xác định 21 điểm landmark
PyAutoGUI (tuỳ chọn)	Điều khiển chuột, bàn phím
Serial / PySerial (tuỳ chọn)	Gửi lệnh đến vi điều khiển (Arduino, ESP32, v.v.)
```
## 🧩 Cấu trúc thư mục

``` css
hand-control/
│
├── src/
│   ├── main.py           # Chương trình chính
│   ├── hand_detector.py  # Lớp phát hiện bàn tay
│   ├── gestures.py       # Xử lý cử chỉ và hành động
│   ├── serial_control.py # Giao tiếp với thiết bị ngoài (nếu có)
│
├── requirements.txt      # Danh sách thư viện
├── README.md             # Tài liệu dự án
└── output/               # Ảnh hoặc log kết quả
```
## ⚙️ Cài đặt
1️⃣ Clone dự án
``` css
git clone https://github.com/yourname/hand-control.git
cd hand-control
```
2️⃣ Cài thư viện cần thiết
```css
pip install -r requirements.txt
```

` 📄 File requirements.txt ví dụ:
``` css
opencv-python
mediapipe
pyautogui
pyserial
numpy
```
## ▶️ Chạy chương trình
``` python
python src/main.py
```

💡 Khi chạy, camera sẽ bật lên.
Di chuyển tay trước camera để xem hệ thống nhận diện và phản ứng.

## 🧰 Mở rộng

- Kết nối với Arduino để điều khiển servo motor / LED / robot arm

- Kết hợp với MediaPipe Pose để điều khiển toàn thân

- Huấn luyện thêm mô hình gesture bằng TensorFlow Lite

## 👨‍💻 Tác giả

Đạt Thành                                                                          
📧 Liên hệ: [thanhdat.developer@gmail.com]                                             
📅 Năm: 2025


