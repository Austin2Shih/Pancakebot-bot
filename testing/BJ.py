from image_processing import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Default.migrated\AppData\Local\Tesseract-OCR\tesseract.exe'

cards = {'a': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 11, 'q': 12, 'k': 13}
def read_bj():
    text = scan_paragraph(find_first_bj())
    text = text.lower()
    print(text)
    if text.split()[0] == 'you':
        return read_end(text)
    else:
        return read_normal(text)

def read_end(text):
    text = text[text.find('your hand') + 10: text.find('cards remaining') + 22]
    your_cards_text = text[:text.find('value')].strip()
    text = text[text.find('dealer hand') + 11:]
    dealer_cards_text = text[: text.find('value') - 2]
    your_cards = [cards[num] for num in your_cards_text if num in cards]
    dealer_cards = [cards[num] for num in dealer_cards_text if num in cards]
    cards_left = int(text[text.find('remaining') + 11: text.find('|')].strip())
    # print(your_cards_text)
    # print(dealer_cards_text)
    return (your_cards, dealer_cards, cards_left)

def read_normal(text):
    text = text[text.find('dealer hand') + 12: text.find('cards remaining') + 22]
    your_cards_text = text[:text.find('xx') - 4]
    dealer_cards_text = text[text.find('xx') - 6: text.find('xx') - 4]
    your_cards = [cards[num] for num in your_cards_text if num in cards]
    dealer_cards = [int(dealer_cards_text.strip())]
    cards_left = int(text[text.find('remaining') + 11: text.find('|')].strip())
    print(your_cards_text)
    print(dealer_cards_text)
    return (your_cards, dealer_cards, cards_left)

print(read_bj())