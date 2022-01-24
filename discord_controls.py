from pynput.keyboard import Key, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController
from time import sleep
# from setup import *

keyboard = keyboardController()
mouse = mouseController()

# Enters a message into the discord text box
# and scrolls to make sure we are always looking
# at the newest messages.
def type_in(string):
    reset()
    keyboard.type(string)
    keyboard.press(Key.enter)
    sleep(0.5)
    mouse.scroll(0, -400)
    
# clicks the continue button
def click_continue():
    mouse.position = (357, 950)
    sleep(0.01)
    mouse.click(Button.left, 2)

# clicks the stop button
def click_stop():
    mouse.position = (400, 950)
    sleep(0.01)
    mouse.click(Button.left, 2)

# resets the mouse position to default
def reset():
    mouse.position = (357, 1000)
    sleep(0.01)
    mouse.click(Button.left, 2)
    sleep(0.01)
    mouse.position = (1000, 950)