from tkinter import *


def button_clicked():
    my_label_1['text'] = input_name.get()


window = Tk()
window.title('Welcome to GUI')
window.minsize(width=500, height=500)

# Add a new label to top
my_label_1 = Label(text='Top Label', font=('Arial', 20))
my_label_1.grid(column=0, row=0)

# Add a button
button = Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

# Add a new button
new_button = Button(text='Click Me', command=button_clicked)
new_button.grid(column=2, row=0)

# Add a input field
input_name = Entry()
input_name.grid(column=3, row=2)

window.mainloop()
