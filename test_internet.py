import tkinter as tk
from tkinter import ttk
import speedtest
import threading
import time
from datetime import datetime

def animate_speed(label, target):
    value = 0
    step = target / 50  # chia nhỏ để animation mượt
    while value < target:
        value += step
        label.config(text=f"{value:.2f} Mbps")
        time.sleep(0.02)
    label.config(text=f"{target:.2f} Mbps")


def run_speed_test():
    try:
        progress.start(10)
        status_label.config(text="🔍 Đang tìm server...")

        st = speedtest.Speedtest()
        st.get_servers([])
        best = st.get_best_server()

        server_info = f"{best['host']} ({best['name']}, {best['country']})"
        server_label.config(text=server_info)

        status_label.config(text="⬇️ Đang đo Download...")
        download = st.download() / 1_000_000

        animate_speed(download_label, download)

        status_label.config(text="⬆️ Đang đo Upload...")
        upload = st.upload() / 1_000_000

        animate_speed(upload_label, upload)

        ping = st.results.ping
        ping_label.config(text=f"{ping:.2f} ms")

        # đánh giá mạng
        if download > 50:
            quality = "💪 Mạng mạnh"
        elif download > 10:
            quality = "😐 Mạng trung bình"
        else:
            quality = "🐢 Mạng yếu"

        status_label.config(text=f"✅ {quality}")

        # lưu lịch sử
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} | {download:.2f} | {upload:.2f} | {ping:.2f}\n")

    except Exception as e:
        status_label.config(text=f"❌ Lỗi: {e}")
    finally:
        progress.stop()


def start_test():
    threading.Thread(target=run_speed_test).start()


# ===== GUI =====
root = tk.Tk()
root.title("Internet Speed Test")
root.geometry("450x380")
root.resizable(False, False)
root.configure(bg="#121212")

# Title
title = tk.Label(root, text="🚀 INTERNET SPEED TEST USING PYTHON ",
                 fg="#00FFFF", bg="#121212")
title.pack(pady=10)

# Button
start_btn = tk.Button(root, text="START TEST", command=start_test,
                      font=("Arial", 12, "bold"),
                      bg="#00C853", fg="white", padx=15, pady=5)
start_btn.pack(pady=10)

# Progress
progress = ttk.Progressbar(root, orient="horizontal",
                           length=300, mode="indeterminate")
progress.pack(pady=10)

# Status
status_label = tk.Label(root, text="Nhấn START để bắt đầu",
                        font=("Arial", 10),
                        fg="white", bg="#121212")
status_label.pack()

# Server
tk.Label(root, text="🌐 Server:",
         font=("Arial", 10, "bold"),
         fg="#00FFFF", bg="#121212").pack(pady=(10, 0))

server_label = tk.Label(root, text="--",
                        font=("Arial", 9),
                        fg="white", bg="#121212")
server_label.pack()

# Result frame
frame = tk.Frame(root, bg="#121212")
frame.pack(pady=15)

def create_row(text, row):
    tk.Label(frame, text=text, font=("Arial", 12),
             fg="white", bg="#121212").grid(row=row, column=0, padx=10, pady=5)

    label = tk.Label(frame, text="--", font=("Arial", 12, "bold"),
                     fg="#00E676", bg="#121212")
    label.grid(row=row, column=1, padx=10)
    return label

download_label = create_row("⬇️ Download:", 0)
upload_label = create_row("⬆️ Upload:", 1)
ping_label = create_row("📡 Ping:", 2)

# Footer
footer = tk.Label(root, text="Made by Xuân Kiên 😎",
                  font=("Arial", 8),
                  fg="gray", bg="#121212")
footer.pack(side="bottom", pady=5)

root.mainloop()