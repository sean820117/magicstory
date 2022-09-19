import keyboard
import time

keyboard.start_recording()
time.sleep(10)
events = keyboard.stop_recording()
keyboard.replay(events)
for e in events:
  print(e.to_json())
