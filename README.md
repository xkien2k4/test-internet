#  Internet Speed Test (Python)

Ứng dụng **kiểm tra tốc độ Internet** với giao diện GUI đơn giản sử dụng Python.
Đo các thông số:

*  Download speed
*  Upload speed
*  Ping
*  Server đang sử dụng

---

##  Demo

Giao diện gồm:

* Nút **START TEST**
* Thanh progress animation
* Hiển thị tốc độ Download / Upload / Ping
* Lưu lịch sử test

---

##  Yêu cầu

* Python **3.10.11**
* Pip

---

##  Cài đặt 
Cài đặt:

```bash
pip install -r requirements.txt
```

---

##  Cách chạy chương trình

```bash
python main.py
```

---

##  Công nghệ sử dụng

* `tkinter` → giao diện GUI (có sẵn trong Python)
* `speedtest-cli` → đo tốc độ mạng
* `threading` → chạy test không làm lag UI
* `datetime` → lưu lịch sử
* `time` → animation

---

##  Tính năng

*  Giao diện GUI dễ dùng
*  Animation tốc độ mượt
*  Hiển thị server test
*  Đánh giá chất lượng mạng
*  Lưu lịch sử vào file `history.txt`

---

## 📊 Đánh giá tốc độ

| Download     | Đánh giá      |
| ------------ | ------------- |
| > 50 Mbps    | 💪 Mạng mạnh  |
| 10 - 50 Mbps | 😐 Trung bình |
| < 10 Mbps    | 🐢 Mạng yếu   |

---

##  Lưu lịch sử

Sau mỗi lần test, dữ liệu được lưu vào:

```
history.txt
```

Format:

```
YYYY-MM-DD HH:MM:SS | Download | Upload | Ping
```

---

##  Lưu ý

* Cần kết nối Internet để test
* Lần test đầu có thể hơi lâu do tìm server
* Không đóng app khi đang đo

---

##  Tác giả

** Nguyễn Vũ Xuân Kiên **

Pull request luôn được chào đón! 🚀
