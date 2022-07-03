"""
3.1.1.2 LAB: A very simple calculator
https://edube.org/learn/pcpp1-4-gui-programming/lab-a-very-simple-calculator
You need a calculator. A very simple and very specific calculator. Look at the picture - it contains two fields that the
user can use to enter arguments, a radio button to select the operation to perform, and a button initiating
the evaluation:
We expect the calculator to behave in the following way:
- if both fields contain valid (integer or float) numbers, clicking the Evaluate button should display an info window
showing the evaluation's result;
- if any of the fields contains invalid data (e.g., a string, or a field is empty), clicking the Evaluate button should
present an error window describing the problem, and the focus should be moved to the field causing the problem.
Don't forget to protect your code from dividing by zero, and use the grid manager to compose the window interior.
"""
import tkinter as tk
from tkinter import messagebox


def set_string_1(*args):
    global last_string_1
    string = text_1.get()
    last_string_1 = string


def set_string_2(*args):
    global last_string_2
    string = text_2.get()
    last_string_2 = string


def evaluate(*args):
    global last_string_1
    global last_string_2
    input_error_flag = 0
    try:
        left_operand = float(last_string_1)
        input_error_flag = 1
        right_operand = float(last_string_2)
        if switch.get() == 0:
            result = left_operand + right_operand
            messagebox.showinfo(title='Result', message=f'{result}')
        elif switch.get() == 1:
            result = left_operand - right_operand
            messagebox.showinfo(title='Result', message=f'{result}')
        elif switch.get() == 2:
            result = left_operand * right_operand
            messagebox.showinfo(title='Result', message=f'{result}')
        elif switch.get() == 3:
            try:
                result = left_operand / right_operand
                messagebox.showinfo(title='Result', message=f'{result}')
            except ZeroDivisionError:
                entry_2.focus_set()
                messagebox.showerror(title='Result', message='ZeroDivisionError')
    except ValueError:
        if input_error_flag == 0:
            entry_1.focus_set()
            messagebox.showerror(title='Result', message="Wrong type of left operand.")
        else:
            entry_2.focus_set()
            messagebox.showerror(title='Result', message="Wrong type of right operand.")


window = tk.Tk()
last_string_1 = ''
last_string_2 = ''
text_1 = tk.StringVar()
text_2 = tk.StringVar()
text_1.set(last_string_1)
text_1.trace('w', set_string_1)
text_2.set(last_string_2)
text_2.trace('w', set_string_2)
entry_1 = tk.Entry(window, width=20, textvariable=text_1)
entry_2 = tk.Entry(window, width=20, textvariable=text_2)
button_1 = tk.Button(window, text="Evaluate", command=evaluate)
switch = tk.IntVar()
switch.set(0)
radiobutton_1 = tk.Radiobutton(window, text="+", width=5, variable=switch, value=0)
radiobutton_2 = tk.Radiobutton(window, text="-", width=5, variable=switch, value=1)
radiobutton_3 = tk.Radiobutton(window, text="*", width=5, variable=switch, value=2)
radiobutton_4 = tk.Radiobutton(window, text="/", width=5, variable=switch, value=3)
button_1.grid(row=4, column=1)
radiobutton_1.grid(row=0, column=1)
radiobutton_2.grid(row=1, column=1)
radiobutton_3.grid(row=2, column=1)
radiobutton_4.grid(row=3, column=1)
entry_1.grid(row=2, column=0)
entry_2.grid(row=2, column=2)
window.mainloop()
