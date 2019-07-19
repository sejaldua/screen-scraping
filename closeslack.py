import pyautogui
print("Press Ctrl-C to quit.")
try:
        pyautogui.moveTo(345, 884)
        pyautogui.click()
        #pyautogui.hotkey('ctrl', 'c')
        pyautogui.moveTo(315, 818)
        pyautogui.click()
        pyautogui.keyDown('command')
        pyautogui.press('q')
        pyautogui.keyUp('command')
except KeyboardInterrupt:
        print('\nDone.')