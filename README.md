# screen-scraping
Automating my computer using the `pyautogui` library. Coolest application: automatically set my screen saver to be National Geographic's Photo Of The Day.

### Files
- autoguitest.py: A python script to display the x and y coordinates of the cursor in live time. This script was really helpful whenever I needed to move to a pixel on the screen using the `pyautogui.moveTo(x, y)` function

- closeslack.py: A python script to automatically close the Slack application. This was just a baby step for me as I was playing around with applications of the `pyautogui` library.

- spoti.py: A python script to automatically open the Spotify application... another baby step.

- viewslideshow.png: A photo of a characteristic fraction of the screen on National Geographic's Photo of the Day webpage. This was essential in order to implement the `pyautogui.locateCenterOnScreen([image])` function, which algorithmically searches for the image passed into the function and returns its center coordinates.

- potd.py: 
