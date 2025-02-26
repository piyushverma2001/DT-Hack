#!/usr/bin/env python3

import pyautogui
import random
import time

def main():
    screen_width, screen_height = pyautogui.size()
    while True:
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)        
        pyautogui.moveTo(x, y, duration=1.0)
        time.sleep(60)

if __name__ == "__main__":
    main()
