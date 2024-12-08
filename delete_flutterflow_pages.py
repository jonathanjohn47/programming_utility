import time

import pyautogui

left_click_position = (140, 303)
right_click_position = (140, 303)
delete_click_position = (302, 448)
yes_click_position = (816, 531)

if __name__ == "__main__":
    time.sleep(5)
    for i in range(20):
        pyautogui.click(left_click_position)
        time.sleep(1)
        pyautogui.rightClick(right_click_position)
        time.sleep(1)
        pyautogui.click(delete_click_position)
        time.sleep(1)
        pyautogui.click(yes_click_position)
        time.sleep(1)
