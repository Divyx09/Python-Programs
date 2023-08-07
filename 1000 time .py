import time
import pyautogui

time.sleep(4)
count=0
while count<=1000:
    pyautogui.typewrite("  "+str(count))
    pyautogui.press("enter")
    count=count+1
