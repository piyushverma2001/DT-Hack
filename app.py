#!/usr/bin/env python3

import pyautogui
import random
import time

MOVE_DURATION = 1.0
SLEEP_INTERVAL = 60

def main():
    screen_width, screen_height = pyautogui.size()
    
    try:
        while True:
            x = random.randint(0, screen_width - 1)
            y = random.randint(0, screen_height - 1)
            print(f"Moving mouse to ({x}, {y})")
            pyautogui.moveTo(x, y, duration=MOVE_DURATION)
            time.sleep(SLEEP_INTERVAL)
    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    main()
