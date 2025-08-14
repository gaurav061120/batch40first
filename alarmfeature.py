import tkinter as tk
import time
import threading
from tkinter import messagebox

# Alarm check function
def check_alarm():
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time.get():
            messagebox.showinfo("Alarm", "Time to wake up! ⏰")
            break
        time.sleep(1)

# Function to update the clock display
def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Set alarm button click
def set_alarm():
    t = threading.Thread(target=check_alarm)
    t.daemon = True
    t.start()

# Main window
root = tk.Tk()
root.title("Clock with Alarm")
root.geometry("300x200")
root.resizable(False, False)

# Clock display
clock_label = tk.Label(root, font=("Arial", 40), fg="white", bg="black")
clock_label.pack(pady=10)

# Alarm input
alarm_time = tk.StringVar()
tk.Label(root, text="Set Alarm (HH:MM:SS):").pack()
tk.Entry(root, textvariable=alarm_time, font=("Arial", 14), justify="center").pack()

# Set alarm button
tk.Button(root, text="Set Alarm", command=set_alarm).pack(pady=10)

# Start updating the clock
update_time()

root.mainloop()
