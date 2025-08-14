import tkinter as tk
import time

# Function to update time
def update_time():
    current_time = time.strftime("%H:%M:%S")  # Get current time in HH:MM:SS format
    label.config(text=current_time)  # Update label text
    label.after(1000, update_time)   # Call this function again after 1 second

# Create the window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("250x100")
root.resizable(False, False)

# Clock label styling
label = tk.Label(root, font=("Arial", 40), fg="white", bg="black")
label.pack(anchor="center")

# Start clock
update_time()

# Run the GUI loop
root.mainloop()

