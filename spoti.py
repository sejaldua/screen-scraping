import pyautogui
print("Press Ctrl-C to quit.")
try:
        pyautogui.moveTo(940, 883)
        pyautogui.click()
        #pyautogui.hotkey('ctrl', 'c')
        loc = pyautogui.locateCenterOnScreen('oranges.png')
        print(loc)
        #pyautogui.moveTo(loc)
        pyautogui.keyDown('ctrl')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')
except KeyboardInterrupt:
        print('\nDone.')