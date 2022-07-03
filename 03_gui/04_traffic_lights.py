"""
3.1.1.5 LAB: Traffic lights
https://edube.org/learn/pcpp1-4-gui-programming/lab-traffic-lights
Look at the snippet in the editor - can you see that mysterious tuple consisting of four three-element tuples? Can you
guess what information it carries?
It's a set of rules describing the behavior of British-style traffic lights. Assume that the very first element of all
inner tuples is assigned to the red light, the second - to the yellow, and the third - to the green one. True means that
the light is on, False - off.
As you see, there are four different phases:
    the red light is lit,
    the red and yellow lights are lit together,
    the green light is lit,
    the yellow light is lit.
Your task is to implement a model which will show how such a traffic signal works. The model should look as follows:
Red Red-Yellow Green Yellow
As you see, the model is built of three widgets:
    the canvas being a background for all the three lights,
    the button named "Next" - clicking it switches the signal to the next phase,
    the button named "Quit" - clicking it immediately exits the program.
Note: use the phases tuple as a "knowledge base" for your whole code. The code has to adopt to any change done to the
tuple, e.g., there can be more or less than four phases and the lights' combinations can be different also.
If traffic lights in your home country work in a different way, you can implement your native scheme, but the only
change you're allowed to make is to modify the phases tuple - the code itself must remain the same.
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
