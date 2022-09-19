import keyboard
import time

# Sends 20 "key down" events in 0.1 second intervals, followed by a single
# "key up" event.
for i in range(10):
    keyboard.press('a')
    time.sleep(1)
keyboard.release('a')
