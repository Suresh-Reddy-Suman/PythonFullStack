import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    canvas.itemconfig(timer_value, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(20)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time):
    minutes = math.floor(time / 60)
    seconds = time % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_value, text=f'{minutes}:{seconds}')
    if time > 0:
        window.after(1000, count_down, time - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro App')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=220, height=230, bg=YELLOW, highlightthickness=0)
tomata = PhotoImage(file='tomato.png')
canvas.create_image(110, 112, image=tomata)
timer_value = canvas.create_text(110, 125, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)
canvas.update()

check_mark = '✔'

start = Button(text='Start', command=start_timer)
start.grid(column=0, row=2)

timer = Label(text='TIMER', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

checkbox = Label(text=check_mark, font=(10), fg=GREEN, bg=YELLOW)
checkbox.grid(column=1, row=3)

reset = Button(text='Reset', command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
