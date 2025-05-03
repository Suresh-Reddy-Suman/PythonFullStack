import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ----------------Fetch Details----------------------------#

def fetch_details():
    with open('./file.json', mode='r') as password_data:
        data = json.load(password_data)
        website_value = website_input.get()
        if website_value not in data:
            messagebox.showerror(title='No details',message='No details found')
        else:
            messagebox.showinfo("Password Details",
                                f"Username :{data[website_input.get()]['Username']}\nPassword:{data[website_input.get()]['Password']}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    output_password = ""
    for char in password_list:
        output_password += char

    password_input.insert(END, f'{output_password}')
    pyperclip.copy(output_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_text = website_input.get()
    email_text = email_input.get()
    password_text = password_input.get()

    new_data = {
        website_text: {
            'Username': email_text,
            'Password': password_text
        }
    }
    if len(website_text) == 0 or len(email_text) == 0 or len(password_text) == 0:
        messagebox.showerror(title="Incorrect Details ", message='Please fill the details before we add')
    else:
        try:
            with open('file.json', mode='r') as file:
                data = json.load(file)
        except:
            with open('file.json', mode='w') as file:
                json.dump({}, file)
        else:
            with open('file.json', mode='r') as file:
                data = json.load(file)
            with open('file.json', mode='w') as new_version:
                data.update(new_data)
                json.dump(data, new_version, indent=4)

        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Safe Password Generator')
window.config(padx=100, pady=50)
logo = PhotoImage(file='logo.png')
screen = Canvas(width=200, height=189)
screen.create_image(100, 95, image=logo)
screen.grid(column=1, row=0)

# Create Label
website = Label(text='Website:')
website.grid(column=0, row=1)

email_username = Label(text='Email/Username:')
email_username.grid(column=0, row=2)

password = Label(text='Password: ')
password.grid(column=0, row=3)

# Create Input fields
website_input = Entry(width=30)
website_input.grid(column=1, row=1)

search = Button(text='Search', width=12, command=fetch_details)
search.grid(column=2, row=1)

email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=30)
password_input.grid(column=1, row=3)

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=45, pady=2, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
