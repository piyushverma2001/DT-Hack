#!/usr/bin/env python3

import pyautogui
import random
import time
import threading
import tkinter as tk
from tkinter import messagebox

class MouseMoverApp:
    def __init__(self, master):
        self.master = master
        master.title("Mouse Mover")

        self.move_duration = 1.0
        self.sleep_interval = 60.0

        tk.Label(master, text="Move Duration (sec):").grid(row=0, column=0, padx=10, pady=10)
        self.entry_duration = tk.Entry(master)
        self.entry_duration.insert(0, str(self.move_duration))
        self.entry_duration.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(master, text="Sleep Interval (sec):").grid(row=1, column=0, padx=10, pady=10)
        self.entry_interval = tk.Entry(master)
        self.entry_interval.insert(0, str(self.sleep_interval))
        self.entry_interval.grid(row=1, column=1, padx=10, pady=10)

        self.start_button = tk.Button(master, text="Start", command=self.start_moving)
        self.start_button.grid(row=2, column=0, padx=10, pady=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_moving, state=tk.DISABLED)
        self.stop_button.grid(row=2, column=1, padx=10, pady=10)

        self.running = False
        self.thread = None
        self.stop_event = threading.Event()

    def start_moving(self):
        try:
            self.move_duration = float(self.entry_duration.get())
            self.sleep_interval = float(self.entry_interval.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for duration and interval.")
            return

        self.running = True
        self.stop_event.clear()
        self.thread = threading.Thread(target=self.move_mouse, daemon=True)
        self.thread.start()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_moving(self):
        self.running = False
        self.stop_event.set()
        if self.thread is not None:
            self.thread.join()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def move_mouse(self):
        screen_width, screen_height = pyautogui.size()
        while self.running and not self.stop_event.is_set():
            x = random.randint(0, screen_width - 1)
            y = random.randint(0, screen_height - 1)
            print(f"Moving mouse to ({x}, {y})")
            pyautogui.moveTo(x, y, duration=self.move_duration)
            total_slept = 0
            while total_slept < self.sleep_interval:
                if self.stop_event.is_set():
                    break
                time.sleep(0.1)
                total_slept += 0.1
        print("Mouse mover stopped.")

def main():
    root = tk.Tk()
    app = MouseMoverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
