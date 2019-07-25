import pyautogui, time
import datetime
import subprocess
import applescript

print("Press Ctrl-C to quit.")

# the screen scraping function
def getpotd():

    # open chrome via spotlight
    pyautogui.moveTo(1345, 12)  
    pyautogui.click()
    pyautogui.typewrite('chrome', interval=0.05)
    pyautogui.keyDown('return')
    time.sleep(0.05)
    pyautogui.keyUp('return')

    # navigate to Nat Geo Photo of the Day in new tab
    pyautogui.keyDown('command')
    pyautogui.keyDown('t')
    time.sleep(0.2)
    pyautogui.keyUp('t')
    pyautogui.keyUp('command')
    time.sleep(1)
    pyautogui.typewrite('https://www.nationalgeographic.com/photography/photo-of-the-day/', interval=0.03)
    pyautogui.keyDown('return')
    time.sleep(0.05)
    pyautogui.keyUp('return')
    time.sleep(1)

    # maximize screen using a tool called Magnet
    # note: this is essential in order to be able to navigate
    # to specific coordinates on the screen
    pyautogui.moveTo(1049, 9)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click(1103, 368)
    pyautogui.moveTo(800, 368)
    time.sleep(1)

    # scroll down and click on "View Slideshow" to expand the image
    pyautogui.scroll(-10, pause=1)
    time.sleep(1)
    x, y = pyautogui.locateCenterOnScreen('viewslideshow.png')
    pyautogui.moveTo(int(x/2), int(y/2))
    print("about to click")
    time.sleep(0.3)
    pyautogui.click(button='left')
    time.sleep(2)

    #go_to_old_photo()

    # take screenshot using keyboard shortcut (Cmd + Shift + 4)
    pyautogui.keyDown('command')
    pyautogui.keyDown('shift')
    time.sleep(0.2)
    pyautogui.keyDown('4')
    time.sleep(0.2)
    pyautogui.keyUp('4')
    time.sleep(0.1)
    pyautogui.keyUp('shift')
    pyautogui.keyUp('command')
    pyautogui.moveTo(462, 213)
    pyautogui.dragTo(1285, 791, 3, button='left')

    # get the current date in order to recreate screenshot filepath
    # TODO: make this cleaner using string formatting and datetime library funcs
    now = datetime.datetime.now()
    if (now.hour < 12):
        append = 'AM'
        hour = now.hour
    elif (now.hour == 12):
        append = 'PM'
        hour = 12
    else:
        hour = now.hour % 12
        append = 'PM'
    name = 'Screen\\ Shot\\ ' + str(now.year) + '-' + \
           '%0*d' % (2, now.month) + '-' + '%0*d' % (2, now.day) + \
           '\\ at\\ ' + str(hour) + '.' + '%0*d' % (2, now.minute) + \
           '.' + '%0*d' % (2, now.second) + '\\ ' + append + '.png'
    print(name)

    # here, I have implemented a workaround... I can't use my osascript
    # unless the filepath does not have spaces in it, so I must rename
    # the Screen Shot programmatically (using the 'mv' command in Terminal)

    # go back to Terminal/iTerm application
    pyautogui.keyDown('command')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('command')
    time.sleep(1)

    # open up a new Terminal/iTerm tab
    pyautogui.keyDown('command')
    pyautogui.keyDown('t')
    pyautogui.keyUp('t')
    pyautogui.keyUp('command')
    pyautogui.typewrite('cd Desktop', interval=0.03)
    pyautogui.keyDown('return')
    time.sleep(0.05)
    pyautogui.keyUp('return')

    # wait for screenshot to be saved in Finder
    pyautogui.moveTo(1345, 12)
    pyautogui.click()
    pyautogui.typewrite('finder', interval=0.05)
    pyautogui.keyDown('return')
    time.sleep(0.05)
    pyautogui.keyUp('return')
    time.sleep(6)   # takes roughly 6 seconds

    # go back to Terminal / iTerm
    pyautogui.keyDown('command')
    pyautogui.keyDown('tab')
    time.sleep(0.1)
    pyautogui.keyUp('tab')
    pyautogui.keyUp('command')

    # renaming the file and exiting out of Terminal / iTerm tab
    newname = 'screensaver' + str(now.month) + '-' + str(now.day) + '-' + str(now.year) + '.png'
    toType = 'mv ' + name + ' ' + newname
    pyautogui.typewrite(toType, interval = 0.05)
    pyautogui.keyDown('return')
    time.sleep(0.05)
    pyautogui.keyUp('return')
    time.sleep(1)
    pyautogui.typewrite('exit', interval = 0.08)
    pyautogui.keyDown('return')
    time.sleep(0.05)
    pyautogui.keyUp('return')
    return newname

# get yesterday's photo
def go_to_old_photo():
    pyautogui.moveTo(1412, 477)
    pyautogui.click()
    time.sleep(1)

# figuring out how to close the Terminal tab
def test_new_terminal_tab():
    time.sleep(2)
    print("opening new tab")
    time.sleep(1)
    pyautogui.keyDown('command')
    pyautogui.keyDown('t')
    pyautogui.keyUp('t')
    pyautogui.keyUp('command')
    pyautogui.typewrite('cd Desktop', interval = 0.05)
    pyautogui.keyDown('return')
    time.sleep(0.05)
    pyautogui.keyUp('return')
    time.sleep(1)
    pyautogui.typewrite('exit', interval = 0.08)
    pyautogui.keyDown('return')
    time.sleep(0.05)
    pyautogui.keyUp('return')
    time.sleep(1)
    pyautogui.keyDown('return')
    time.sleep(0.05)
    pyautogui.keyUp('return')

# using subprocess and osascripting to programmatically set desktop background to filepath parameter
def set_desktop_background(filename):
    SCRIPT = '''/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to POSIX file "%s"
    end tell
    END
    '''
    subprocess.Popen(SCRIPT%filename, shell=True)
    time.sleep(2)
    pyautogui.keyDown('control')
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    pyautogui.keyUp('control')
    time.sleep(2.5)
    pyautogui.keyDown('backspace')


#test_new_terminal_tab()
partialpath = '/Users/sejaldua/Desktop/'
name = getpotd()
fpath = partialpath + name
print("Setting screen saver to: " + fpath)
set_desktop_background(fpath)
