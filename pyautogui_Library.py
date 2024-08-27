import pyautogui
import sys

# screen size
#w,h = pyautogui.size()
#print(w, " ", h)

# mouse function
#pyautogui.moveTo(1200,300,duration=3) # move to position
#pyautogui.moveRel(0,-150,duration=3) # move to relative

# mouse click
#pyautogui.click(700,400,duration=2)
#pyautogui.doubleClick(1300,400,duration=2)
#pyautogui.rightClick(1300,400,duration=2)

# scrolling -: down, +: up
#pyautogui.scroll(-50)

# ketboard
#pyautogui.typewrite("Hello world!", interval=0.5)
#pyautogui.press("win")
#pyautogui.hotkey("alt","tab")

# scrennshot
#screenshot = pyautogui.screenshot()
#screenshot.save()
#pyautogui.screenshot().save("ss.png")

win10 = pyautogui.screenshot(region=(0, 1041, 50, 39))
location = pyautogui.locateOnScreen(win10)
pyautogui.moveTo(location)