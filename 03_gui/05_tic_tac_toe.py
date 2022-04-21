"""
3.1.1.6 LAB: Tic-Tac-Toe
https://edube.org/learn/pcpp1-4-gui-programming/lab-tic-tac-toe
"""
import tkinter as tk
from tkinter import messagebox
import random


def is_draw():
    if len(available_tails) == 0:
        messagebox.showinfo(title='Game Over!', message="It's a draw!")
        window.destroy()


def check_winner():
    for combination in usr_win_combinations:
        if all(item in user_choices for item in combination):
            messagebox.showinfo(title='Game Over!', message='I won!')
            window.destroy()
    for combination in comp_win_combinations:
        if all(item in computer_choices for item in combination):
            messagebox.showinfo(title='Game Over!', message='Computer won!')
            window.destroy()


def computer_move():
    choice = random.choice(available_tails)
    exec(f'global b_{choice}')
    exec(f'canvas_cmp = tk.Canvas(b_{choice})')
    exec('canvas_cmp.create_text(135, 115, text="x", font=("Arial", "80", "bold"), fill="red")')
    exec('canvas_cmp.place(width=264, height=230)')
    computer_choices.append(choice)
    available_tails.remove(choice)
    check_winner()
    is_draw()


def choose(event, arg):
    button_number = arg.cget('wraplength')
    if button_number not in available_tails:
        pass
    else:
        canvas_usr = tk.Canvas(arg)
        canvas_usr.create_text(135, 115, text="o", font=("Arial", "80", "bold"), fill='green')
        canvas_usr.place(width=264, height=230)
        user_choices.append(button_number)
        available_tails.remove(button_number)
        check_winner()
        computer_move()


window = tk.Tk()
window.title("TicTacToe")
comp_win_combinations = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [6, 4, 2]]
usr_win_combinations = [[0, 3, 6], [2, 5, 8], [0, 1, 2], [6, 7, 8]]
available_tails = [0, 1, 2, 3, 5, 6, 7, 8]
computer_choices = [4]
user_choices = []
columns = [0, 1, 2]
rows = [0, 1, 2]
width = 30
height = 13
button_counter = 0
for row in rows:
    for column in columns:
        exec(f'b_{button_counter} = tk.Button(window, wraplength=button_counter, width=width, height=height)')
        exec(f'b_{button_counter}.bind("<Button-1>", lambda event, arg=b_{button_counter}: choose(event, arg))')
        exec(f'b_{button_counter}.grid(row=row, column=column)')
        button_counter += 1
canvas = tk.Canvas(b_4)
canvas.create_text(135, 115, text="x", font=("Arial", "80", "bold"), fill='red')
canvas.place(width=264, height=230)
window.resizable(width=False, height=False)
window.mainloop()
