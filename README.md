# screen-scraping
Automating my computer using the `pyautogui` library. Coolest application: automatically set my screen saver to be National Geographic's Photo Of The Day.

### Files
- autoguitest.py: A python script to display the x and y coordinates of the cursor in live time. This script was really helpful whenever I needed to move to a pixel on the screen using the `pyautogui.moveTo(x, y)` function

- closeslack.py: A python script to automatically close the Slack application. This was just a baby step for me as I was playing around with applications of the `pyautogui` library.

- spoti.py: A python script to automatically open the Spotify application... another baby step.

- viewslideshow.png: A photo of a characteristic fraction of the screen on National Geographic's Photo of the Day webpage. This was essential in order to implement the `pyautogui.locateCenterOnScreen([image])` function, which algorithmically searches for the image passed into the function and returns its center coordinates.

- potd.py: A very long code to automate my computer to do what I want it to do... hehe

Multi-step Process:
> 1. open chrome via spotlight
> 2. navigate to Nat Geo Photo of the Day in new tab
> 3. maximize screen
> 4. scroll down and click "View Slideshow" to maximize the photo
> 5. take a screen shot
> 6. get the current date and format a string to name the screen shot
> 7. go back to Terminal and open up a new tab
> 8. rename the file and close the Terminal tab
The end! Enjoy your new desktop background for the day!


### Code In Action!

![](potd.gif)

[YouTube Video: National Geographic Photo of the Day --> Desktop Picture](https://youtu.be/ytaNkmoTFHg)

### Things I Explored Throughout the Project
-> pyautogui
-> pynput
-> subprocess
-> osascript
-> automator
-> crontab

### A Reflection on Trials and Tribulations


