import random

import pyautogui
import keyboard
import time

mouse_positions = []

t = [0.5,0.8,1]
rt = random.choice(t)

def on_key_event(e):
    global mouse_positions
    if e.name == '1' and e.event_type == keyboard.KEY_DOWN:
        x, y = pyautogui.position()
        mouse_positions.append((x, y))
        print(f"Mouse position saved: x={x}, y={y}")

try:
    while True:
        keyboard.hook(on_key_event)
        keyboard.wait('esc')  # Wait for the 'esc' key to exit the script
except KeyboardInterrupt:
    pass
finally:
    keyboard.unhook_all()
    print("\nScript terminated.")
