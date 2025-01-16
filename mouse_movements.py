import pyautogui
import time

from pyautogui import position

menu_click_position = position(912, 328)
remove_job_position = position(813, 462)

time.sleep(5)
for i in range(2):
    pyautogui.click(menu_click_position)
    time.sleep(1)
    pyautogui.click(remove_job_position)
    time.sleep(3)