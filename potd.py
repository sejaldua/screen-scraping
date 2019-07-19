import pyautogui, time
import datetime
import subprocess
import applescript


print("Press Ctrl-C to quit.")
def getpotd():
    pyautogui.moveTo(1345, 12)    # spotlight
    pyautogui.click()
    pyautogui.typewrite('chrome', interval=0.05)
    pyautogui.keyDown('return')
    time.sleep(0.05)
    pyautogui.keyUp('return')
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
    pyautogui.moveTo(1049, 9)      # magnet
    pyautogui.click()
    time.sleep(1)
    pyautogui.click(1103, 368)
    pyautogui.moveTo(800, 368)
    time.sleep(1)
    pyautogui.scroll(-10, pause=1)
    time.sleep(1)
    x, y = pyautogui.locateCenterOnScreen('viewslideshow.png')
    pyautogui.moveTo(int(x/2), int(y/2))
    print("about to click")
    pyautogui.click(button='left')
    time.sleep(2)

    # yesterday
    #pyautogui.moveTo(1412, 477)    # maximize
    #pyautogui.click()
    #time.sleep(1)


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
    pyautogui.keyDown('command')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
    pyautogui.keyUp('command')
    time.sleep(1)
    pyautogui.keyDown('command')
    pyautogui.keyDown('t')
    pyautogui.keyUp('t')
    pyautogui.keyUp('command')
    pyautogui.typewrite('cd Desktop', interval=0.03)
    pyautogui.keyDown('return')
    time.sleep(0.05)
    pyautogui.keyUp('return')
    pyautogui.moveTo(1345, 12)    # spotlight
    pyautogui.click()
    pyautogui.typewrite('finder', interval=0.05)
    pyautogui.keyDown('return')
    time.sleep(0.05)
    pyautogui.keyUp('return')
    time.sleep(6)
    pyautogui.keyDown('command')
    pyautogui.keyDown('tab')
    time.sleep(0.1)
    pyautogui.keyUp('tab')
    pyautogui.keyUp('command')
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