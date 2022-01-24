from PIL import Image
from pyautogui import locateOnScreen

channel_title = 'Images\\channel_title.png'
pancake = 'Images\\pancake.png'
text_box = 'Images\\text_box.png'

channel_title_bounds = locateOnScreen(channel_title, confidence = 0.98)
text_box_bounds = locateOnScreen(text_box, confidence = 0.98)
message_area_height = channel_title_bounds[1] + text_box_bounds[1]
message_area_width = channel_title_bounds[2]
message_area_bounds = (channel_title_bounds[0], channel_title_bounds[1] + channel_title_bounds[3], 
                        message_area_width, message_area_height)

pic_bounds = locateOnScreen(pancake, confidence = 0.98)
breathing_space = abs(pic_bounds[0] - message_area_bounds[0])
pic_lane_bounds = (message_area_bounds[0], message_area_bounds[1], breathing_space*2 + pic_bounds[2], message_area_height)

reset_point = (text_box_bounds[0] + text_box_bounds[2], text_box_bounds[1] + text_box_bounds[3])
resting_point = (message_area_bounds[0] + message_area_bounds[2], message_area_bounds[1] + message_area_bounds[3])

continue_button = 
stop_button = 