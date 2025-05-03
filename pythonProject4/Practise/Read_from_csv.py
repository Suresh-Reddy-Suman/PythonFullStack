import random

import pandas

selected_card = {}


def new_method():
    global selected_card
    selected_card = random.choice(new_data)
    print(selected_card['English'])


def flash_card():
    print(selected_card['French'])


data = pandas.read_csv('../Project/Day_31_FlashCardProject/data/french_words.csv')
new_data = data.to_dict(orient='records')
print(new_data)

new_method()
flash_card()
