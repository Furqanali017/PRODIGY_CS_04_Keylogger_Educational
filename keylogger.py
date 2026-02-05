import tkinter as tk
from datetime import datetime

def log_key(event):
    key = event.keysym
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs.txt", "a") as file:
        file.write(f"{time_stamp} - {key}\n")

# Create main window
root = tk.Tk()
root.title("Educational Keylogger - Prodigy InfoTech Task 04")
root.geometry("500x300")

label = tk.Label(root, text="Type inside this window to log keystrokes.\n(This logs keys only inside this app)", font=("Arial", 12))
label.pack(pady=20)

# Bind key press event
root.bind("<Key>", log_key)

root.mainloop()
