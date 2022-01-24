from pynput.mouse import Button, Controller
from time import sleep

mouse = Controller()
try:
    while True:
        print(mouse.position)
        sleep(0.1)
except KeyboardInterrupt:
    print('ended')