import tkinter as tk
import random

# ===== BIẾN =====
score = 0
lives = 3
level = 1
time_left = 10
question = (0, 0)
running = True

# ===== ÂM THANH =====
def beep_correct():
    root.bell()

def beep_wrong():
    root.bell()

# ===== GAME =====
def new_question():
    global question, time_left

    if not running:
        return

    a = random.randint(1, level * 2)
    b = random.randint(1, level * 2)
    question = (a, b)

    question_label.config(text=f"{a} x {b} = ?")
    entry.delete(0, tk.END)

    time_left = 20
    update_timer()

def update_timer():
    global time_left, lives, running

    if not running:
        return

    timer_label.config(text=f"⏱️ {time_left}s")

    if time_left <= 0:
        lose_life("⏰ Hết giờ!")
        return

    time_left -= 1
    root.after(1000, update_timer)

def check_answer():
    global score, level

    if not running:
        return

    try:
        user = int(entry.get())
        correct = question[0] * question[1]

        if user == correct:
            score += 1
            level = score // 5 + 1
            result_label.config(text="✅ Đúng!", fg="#00FFAA")
            beep_correct()
        else:
            lose_life(f"❌ Sai! Đáp án: {correct}")
            return

        update_ui()
        new_question()

    except:
        result_label.config(text="⚠️ Nhập số!", fg="orange")

def lose_life(message):
    global lives, running

    lives -= 1
    result_label.config(text=message, fg="red")
    beep_wrong()

    update_ui()

    if lives <= 0:
        running = False
        question_label.config(text="💀 GAME OVER")
        result_label.config(text="Nhấn Restart để chơi lại")
        return

    root.after(1000, new_question)

def update_ui():
    score_label.config(text=f"⭐ Score: {score}")
    lives_label.config(text=f"❤️ Lives: {lives}")
    level_label.config(text=f"📈 Level: {level}")

def reset_game():
    global score, lives, level, running

    score = 0
    lives = 3
    level = 1
    running = True

    result_label.config(text="")
    update_ui()
    new_question()

# ===== GUI =====
root = tk.Tk()
root.title("Multiplication Game PRO")
root.geometry("400x350")
root.configure(bg="#121212")

title = tk.Label(root, text="🧠 MULTIPLICATION PRO",
                 font=("Arial", 16, "bold"),
                 fg="#00FFFF", bg="#121212")
title.pack(pady=10)

# Info
info_frame = tk.Frame(root, bg="#121212")
info_frame.pack()

score_label = tk.Label(info_frame, text="⭐ Score: 0", fg="white", bg="#121212")
score_label.grid(row=0, column=0, padx=10)

lives_label = tk.Label(info_frame, text="❤️ Lives: 3", fg="white", bg="#121212")
lives_label.grid(row=0, column=1, padx=10)

level_label = tk.Label(info_frame, text="📈 Level: 1", fg="white", bg="#121212")
level_label.grid(row=0, column=2, padx=10)

# Timer
timer_label = tk.Label(root, text="⏱️ 10s",
                       font=("Arial", 12),
                       fg="#FFD700", bg="#121212")
timer_label.pack(pady=5)

# Question
question_label = tk.Label(root, text="",
                          font=("Arial", 20, "bold"),
                          fg="white", bg="#121212")
question_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack(pady=5)

check_btn = tk.Button(btn_frame, text="Kiểm tra", command=check_answer,
                      bg="#4CAF50", fg="white", width=12)
check_btn.grid(row=0, column=0, padx=5)

reset_btn = tk.Button(btn_frame, text="Restart", command=reset_game,
                      bg="#f44336", fg="white", width=12)
reset_btn.grid(row=0, column=1, padx=5)

# Result
result_label = tk.Label(root, text="",
                        font=("Arial", 12),
                        bg="#121212")
result_label.pack(pady=5)

# Start game
update_ui()
new_question()

root.mainloop()