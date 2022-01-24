import urllib.request
import json
from html import unescape

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', 
            '4', '5', '6', '7', '8', '9', ' ', ':' ,'&', '!']

def load_dic():
    output = {}
    print()
    for i in range(9, 33):
        if find_count(i) <= 50:
            unreadable_dic = read_file(f"https://opentdb.com/api.php?amount={find_count(i)}&category={i}&difficulty=hard")
            if unreadable_dic['response_code']:
                print(f'response_code was not 0, category: {i}')
            else:
                output[get_category(unreadable_dic)] = get_results(unreadable_dic)
        else:
            while True:
                unreadable_dic = read_file(f"https://opentdb.com/api.php?amount={50}&category={i}&difficulty=hard")
                if unreadable_dic['response_code']:
                    print(f'response_code was not 0, category: {i}')
                else:
                    if get_category(unreadable_dic) not in output:
                        output[get_category(unreadable_dic)] = get_results(unreadable_dic)
                    else:
                        output[get_category(unreadable_dic)].update(get_results(unreadable_dic))
                if len(output[get_category(unreadable_dic)]) >= find_count(i):
                    break
        print(f"Finished loading: {get_category(unreadable_dic)}")
    print("Finished :)\n")
    return output


def remove_punc(string):
    output = ""
    for char in unescape(string).lower():
        if char in alphabet:
            output += char
    return output
    
def get_category(dic):
    return remove_punc(dic['results'][0]['category'])

def get_results(dic):
    output = {}
    for question in dic['results']:
        output[remove_punc(question['question'])] = remove_punc(question['correct_answer'])
    return output

def find_count(cat_num):
    link = "https://opentdb.com/api_count.php?category=" + str(cat_num)
    data = read_file(link)
    return data["category_question_count"]["total_hard_question_count"]

def read_file(link):
    with urllib.request.urlopen(link) as url:
        s = url.read()
        return json.loads(s)

