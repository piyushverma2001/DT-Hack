## Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate
```

## Install modules:
```bash
pip install pyautogui
```

## Ubuntu environments (For Linux only):
```bash
sudo apt-get update
sudo apt-get install python3-tk python3-xlib
```

## Make the Script Executable (optional):
```bash
chmod +x random_mouse_mover.py
```

## Run:
```bash
python app.py
```

## Customize the script:
Movement Duration: The parameter duration=0.5 in pyautogui.moveTo controls how long the mouse takes to move to the random position. You can increase or decrease this as desired.\
Delay Between Movements: The call to time.sleep(2) controls how many seconds to wait between each mouse movement. Increase or decrease this value to change the frequency of random moves.\
Screen Region: By default, the script picks a random position anywhere on the screen. If you want the cursor to move only within a specific area, adjust the random range accordingly.
