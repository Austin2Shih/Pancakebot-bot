from pynput.keyboard import Key, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController
from time import sleep
from image_processing import fishing_rod_alive
from discord_controls import *
from Trivia import trivia

keyboard = keyboardController()
mouse = mouseController()

def fish():
    type_in('p;fish')
    sleep(1.1)
    mouse.scroll(0, -400)
    sleep(1.1)
    mouse.scroll(0, -400)
    if not fishing_rod_alive():
        buy_fishing_rod()
    else:
        sleep(3)

def buy_fishing_rod():
    type_in('p;buy fishing rod')
    sleep(2)
    mouse.scroll(0, -400)
    sleep(0.6)
    click_continue()
    sleep(0.8)
    reset()

def sell_common():
    type_in('p;sell common')
    sleep(2)
    mouse.scroll(0, -400)
    sleep(0.5)
    click_continue()
    sleep(0.9)
    reset()

def work():
    type_in('p;work')
    
def big_loop():
    while True:
        work()
        sleep(0.5)
        sleep(1)
        trivia()
        sleep(1)
        for _ in range(9):
            fish()
try:
    reset()
    big_loop()
 
except KeyboardInterrupt:
    print('finished grinding')
