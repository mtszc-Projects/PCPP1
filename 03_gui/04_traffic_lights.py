"""
3.1.1.5 LAB: Traffic lights
https://edube.org/learn/pcpp1-4-gui-programming/lab-traffic-lights
"""
import tkinter as tk


def set_red():
    return 'red' if phases[tuple_counter][0] else 'gray'


def set_yellow():
    return 'yellow' if phases[tuple_counter][1] else 'gray'


def set_green():
    return 'green' if phases[tuple_counter][2] else 'gray'


def change():
    global tuple_counter
    if tuple_counter == 3:
        tuple_counter = 0
    else:
        tuple_counter += 1
    canvas.create_oval(17.5, 7.5, 17.5 + 115, 7.5 + 115, outline='black', width=5, fill=set_red())
    canvas.create_oval(17.5, 7.5 + 135, 17.5 + 115, 7.5 + 115 + 135, outline='black', width=5, fill=set_yellow())
    canvas.create_oval(17.5, 7.5 + 270, 17.5 + 115, 7.5 + 115 + 270, outline='black', width=5, fill=set_green())


phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))


window = tk.Tk()
tuple_counter = 0
canvas = tk.Canvas(window, width=150, height=400, bg='#4A4A4A')
canvas.create_oval(17.5, 7.5, 17.5+115, 7.5+115, outline='black', width=5, fill=set_red())
canvas.create_oval(17.5, 7.5+135, 17.5+115, 7.5+115+135, outline='black', width=5, fill=set_yellow())
canvas.create_oval(17.5, 7.5+270, 17.5+115, 7.5+115+270, outline='black', width=5, fill=set_green())
next_button = tk.Button(window, text='Next', width=10, command=change)
quit_button = tk.Button(window, text='Quit', width=10, command=window.destroy)
canvas.grid(row=0)
next_button.grid(row=1)
quit_button.grid(row=2)
window.resizable(width=False, height=False)
window.mainloop()
