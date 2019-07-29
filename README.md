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

### Dependencies

`pip install pyautogui`


### Code In Action!

![](video.gif)

[YouTube Video: National Geographic Photo of the Day --> Desktop Picture](https://youtu.be/ytaNkmoTFHg)

### Things I Explored Throughout the Project
>- pyautogui
>- pynput
>- subprocess
>- osascript
>- automator
>- crontab

### A Reflection on Trials and Tribulations

This task could have been accomplished in hundreds of different ways, but I wanted to go about my solution very intentionally. One thing I wanted to personally achieve through this project is an application of apple scripting / use of osascripts. I also wanted to do my best to make the code robust enough to work on someone else's computer. Thus, I had to make sure I wasn't relying on pixel coordinates that only hold true on my personal computer. For example, navigating to Chrome by clicking on the Chrome icon on the dock would not suffice for my purposes. That being said, using an image as a reference point and then using the `pyautogui.locateCenterOnScreen()` function would be perfectly fine. I had some issues with maintaining consistent performance and veering around inadvertent ad pop-ups via automated cursor movements. I also had an issue with naming my screenshot of the Nat Geo photo of the day to a filepath without spaces in it. As you can probably see, my workaround to that involved going back to the Terminal and using the 'mv' command to rename my screenshot. A bug worth mentioning is my osascript execution error which comes up as "136:139: execution error: Can’t get end. (-1728)". I wasn't able to figure out how to make this go away since I am unfamiliar with osascript syntax, but there is no lost functionality despite the bug. My next step for this project is to set up a scheduled linux process so that every morning when I wake up, the screen scraping script executes. 
