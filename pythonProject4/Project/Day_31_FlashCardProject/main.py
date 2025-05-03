import random
import time
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def change():
    global current_card
    current_card = random.choice(final)
    print(current_card)
    canvas.itemconfig(background, image=front)
    canvas.itemconfig(title, text='French')
    canvas.itemconfig(word, text=current_card['French'])
    my_screen.after(3000, flip_card)
    if mark_right:
        final.remove(current_card)
        new_file = pandas.DataFrame(final).to_csv('./data/Updated File')


def flip_card():
    canvas.itemconfig(background, image=back)
    canvas.itemconfig(title, text='English')
    canvas.itemconfig(word, text=current_card['English'])


my_screen = Tk()
# TODO Generate UI

my_screen.title('Welcome to Learning Program')
my_screen.config(width=1000, height=800, bg=BACKGROUND_COLOR)

# TODO : Images
front = PhotoImage(file='./images/card_front.png')
back = PhotoImage(file='./images/card_back.png')
right = PhotoImage(file='./images/right.png')
wrong = PhotoImage(file='./images/wrong.png')

# TODO : Canvas Creation
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
background = canvas.create_image(400, 263, image=front)

title = canvas.create_text(400, 150, text='French', font=('Arial', 25, 'bold'))
word = canvas.create_text(400, 263, text='Word', font=('Arial', 30, 'bold'))
canvas.grid(column=0, row=0, padx=50, pady=50, columnspan=3)

my_screen.after(3000, flip_card)

mark_right = Button(image=right, command=change)
mark_right.grid(column=0, row=1, padx=10, pady=10)

mark_wrong = Button(image=wrong, command=change)
mark_wrong.grid(column=2, row=1, padx=10, pady=10)

## Read Data from csv
try:
    data = pandas.read_csv('./data/Updated File')
    final = data.to_dict(orient='records')
    print('Updated file picked')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')
    final = data.to_dict(orient='records')

change()
my_screen.mainloop()
