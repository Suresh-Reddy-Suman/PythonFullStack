from tkinter import *


def convert_miles_to_km():
    convert_value = int(float(miles_input.get()) * 1.6)
    output.config(text=convert_value)


window = Tk()
window.title('Mile to KM Converter')
window.config(padx=10, pady=10)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=2)
is_equal_to.config(padx=5, pady=5)

miles_input = Entry()
miles_input.config(width=10)
miles_input.grid(column=1, row=1)

output = Label(text=0)
output.grid(column=1, row=2)
output.config(padx=5, pady=5)

calculate = Button(text='Calculate', command=convert_miles_to_km)
calculate.grid(column=1, row=3)
calculate.config(pady=5, padx=5)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=1)
miles_label.config(padx=5, pady=5)

km_label = Label(text='Km')
km_label.grid(column=2, row=2)
km_label.config(padx=5, pady=5)

window.mainloop()
