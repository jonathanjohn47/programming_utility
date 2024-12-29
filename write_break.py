import time
import pyautogui
from datetime import datetime
import subprocess

# Start caffeinate to keep the screen awake
caffeinate_process = subprocess.Popen(['caffeinate'])

click_and_write_point = pyautogui.Point(x=846, y=765)
send_point = pyautogui.Point(x=1259, y=768)

try:
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == "13:35":
            pyautogui.click(click_and_write_point)
            pyautogui.write("Break")
            time.sleep(1)
            pyautogui.moveTo(send_point.x, send_point.y, duration=1)
            pyautogui.click(send_point)
            time.sleep(3600)
            pyautogui.click(click_and_write_point)
            pyautogui.write("Back")
            time.sleep(1)
            pyautogui.moveTo(send_point.x, send_point.y, duration=1)
            break
        time.sleep(30)  # Check every 30 seconds to reduce CPU usage
finally:
    # Terminate caffeinate process to allow the system to sleep again
    caffeinate_process.terminate()
