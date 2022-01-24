import pytesseract
from PIL import Image, ImageOps
import pyautogui
from image_processing import *
from time import sleep
from discord_controls import reset, type_in
from json_processor import load_dic, remove_punc
from html import unescape

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
database = load_dic()

# Function to find, parse, and answer Trivia questions
def trivia():
    type_in('p;trivia hard')
    sleep(2)
    category, question, options = process_prompt(find_first_message())
    while category not in database:
        type_in('p;trivia hard')
        category, question, options = process_prompt(find_first_message())
    category_stuff = database[category]
    answer = category_stuff[find_best_key(question, category_stuff)]
    num_answer = options[find_best_key(answer, options)]
    type_in(str(num_answer))

# Uses the difference score from find_rough_difference to choose an answer.
def find_best_key(key, dic):
    key_list = dic.keys()
    return min(key_list, key = lambda x: find_rough_difference(key.split(), x.split()))

# Compares string 1 and string 2 and gives a difference score.
def find_rough_difference(str1, str2):
    if str1 == str2:
        return 0
    elif not str1 or not str2:
        return max(len(str1), len(str2))
    elif str1[0] == str2[0]:
        return find_rough_difference(str1[1:], str2[1:])
    else:
        if str1[0][0] == str2[0][0]:
            return 1.1 + find_rough_difference(str1[1:], str2[1:])
        else:
            return 1 + find_rough_difference(str1[1:], str2[1:])

# Function to parse through the large text that comes out of the OCR
def process_prompt(image):
    prompt = scan_paragraph(image)[51:]
    prompt = prompt[prompt.find('#') + 6: prompt.find('Say the number of the correct answer.')].strip(' ') + '[5'
    hard_index = prompt.find('HARD')
    options = {}
    for i in range(4):
        if prompt.find('[' + str(i + 1)) != -1:
            brackets = prompt.find('[' + str(i + 1))
        else:
            brackets = prompt.find('(' + str(i + 1))
        if prompt.find('[' + str(i + 2)) != -1:
            next_brackets = prompt.find('[' + str(i + 2))
        else:
            next_brackets = prompt.find('(' + str(i + 2))
        options[remove_punc(prompt[brackets + 3: next_brackets].strip(' '))] = i + 1
    category = remove_punc(prompt[: hard_index - 2].strip(' '))
    if prompt.find('?') != -1:
        first_punc = prompt.find('?')
    else:
        first_punc = prompt.find('.')
    question = remove_punc(prompt[hard_index + 6: first_punc + 1].strip(' '))

    return category, question, options
