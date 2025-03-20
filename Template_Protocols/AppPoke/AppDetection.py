import pyautogui
pyautogui.moveTo(1122,870)
x, y = pyautogui.position()
print(f"Mouse position: {x}, {y}")

''' 
# Get screen size
screenWidth, screenHeight = pyautogui.size()
print(f"Screen size: {screenWidth} x {screenHeight}")

# Get current mouse position
currentMouseX, currentMouseY = pyautogui.position()
print(f"Current mouse position: {currentMouseX}, {currentMouseY}")

# Move mouse to a specific location
pyautogui.moveTo(1122,870)

# Click the mouse
pyautogui.click() #defaults to left click


# Take a screenshot
im1 = pyautogui.screenshot()
im1.save('my_screenshot.png')

#find an image on screen.
location = pyautogui.locateOnScreen('button.png')
print(location)
if location is not None:
    pyautogui.click(location)

#add a delay to slow down actions.
time.sleep(1)'
'''