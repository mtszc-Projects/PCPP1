"""
3.1.1.4 LAB: The clicker
https://edube.org/learn/pcpp1-4-gui-programming/lab-the-clicker
"""
import tkinter as tk
import random


def timer():
    global time_counter
    time_counter += 1
    global label
    label = tk.Label(window, text=time_counter)
    label.grid(row=5, column=2)
    if len(randoms) == 0:
        window.after_cancel(run)
    run = window.after(1000, timer)


def eliminate(event, arg):
    global start
    if start == 0:
        window.after(1000, timer())
        start = 1
    button_value = arg.cget('text')
    if button_value == min(randoms):
        arg['state'] = tk.DISABLED
        randoms.pop()


window = tk.Tk()
start = 0
time_counter = 0
button_counter = 0
columns = [0, 1, 2, 3, 4]
rows = [0, 1, 2, 3, 4]
randoms = random.sample(range(1000), 25)
for row in rows:
    for column in columns:
        exec(f'b_{button_counter} = tk.Button(window, text=randoms[button_counter], width=10)')
        exec(f'b_{button_counter}.bind("<Button-1>", lambda event, arg=b_{button_counter}: eliminate(event, arg))')
        exec(f'b_{button_counter}.grid(row=row, column=column)')
        button_counter += 1
randoms.sort(reverse=True)
label = tk.Label(window, text=time_counter)
label.grid(row=5, column=2)
window.resizable(width=False, height=False)
window.mainloop()
