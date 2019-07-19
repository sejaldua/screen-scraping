import pyautogui
print("Press Ctrl-C to quit.")
try:
        while True:
                x, y = pyautogui.position()
                if (x == 32 and y == 888):
                        pyautogui.click()
                positionStr = "X: " + str(x).rjust(4) + "\tY: " + str(y).rjust(4)
                print(positionStr, end='')
                print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
        print('\nDone.')
