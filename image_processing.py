from time import sleep
import pytesseract
from PIL import Image, ImageOps
import pyautogui
# from setup import *

x_mark_path = 'Images\\x_mark.png'
check_mark_path = 'Images\\check_mark.png'
broken_rod_path = 'Images\\broken_rod1.png'
no_rod_path = 'Images\\broken_rod2.png'
pancake = 'Images\\pancake.png'
blackjack = 'Images\\blackjack.png'

def find_and_mark():
    bounds = (285, 880, 595, 100)
    pic = pyautogui.screenshot(region = bounds)
    pic.save('Images\\test.png')
    found = pyautogui.locateAll(x_mark_path, pic, confidence = 0.95)
    marked_pic = Image.open('Images\\test.png')
    for coords in found:
        new_bounds = (coords[0], coords[1], coords[0] + coords[2], coords[1] + coords[3])
        marked_pic.paste('red', box = new_bounds)
        marked_pic.save('Images\\test_find.png')

# checks to see if any picture (needles) are found in the bounds
def any_found(needles, bounds = (285, 880, 595, 100)):
    pic = pyautogui.screenshot(region = bounds)
    for needle in needles:
        found = pyautogui.locateAll(needle, pic, confidence = 0.80)
        for coords in found:
            return True
    return False

# returns the positions all of the found needles in the bounds
def all_found(needle, bounds = (285, 880, 595, 100)):
    pic = pyautogui.screenshot(region = bounds)
    found = pyautogui.locateAll(needle, pic, confidence = 0.80)
    return found
        
def fishing_rod_alive():
    return not any_found([no_rod_path, broken_rod_path])

def find_first_message():
    #pyautogui.screenshot(region = (280, 100, 60, 875)).show()
    bounds = max(all_found(pancake, bounds = (280, 100, 60, 875)), key = lambda x: x[1])
    new_bounds = (285 + bounds[0] + 45, (100 + bounds[1] + 20), 550, 975 - (100 + bounds[1] + 20))

    return pyautogui.screenshot(region = new_bounds)

def find_first_bj():
    bounds = max(all_found(blackjack, bounds = (335, 100, 700, 875)), key = lambda x: x[1])
    new_bounds = (335, (125 + bounds[1]), 550, 950 - (100 + bounds[1]))
    return pyautogui.screenshot(region = new_bounds)

def scan_paragraph(image):
    test = ImageOps.expand(ImageOps.invert(image.convert("RGB")), (10, 10, 10, 10), fill = 'BLUE')
    test = test.resize((test.width*3, test.height*3))
    text = pytesseract.image_to_string(test)
    text = text.replace("\n", " ").rstrip("\x0c").strip(' ')
    return text
