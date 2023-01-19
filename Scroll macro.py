import pyautogui
import time
import keyboard

running = True
scrollSpeed = -60

while True:    
    while running:
        if keyboard.is_pressed('shift'):
            running = False
            time.sleep(1)
        elif keyboard.is_pressed('space'):
            pyautogui.scroll(-5)
        else:
            pyautogui.scroll(scrollSpeed)
        if keyboard.is_pressed('up'):
            scrollSpeed += 5
        if keyboard.is_pressed('down'):
            scrollSpeed -= 5
    if keyboard.is_pressed('shift'):
        running = True
        time.sleep(1)
        

    
