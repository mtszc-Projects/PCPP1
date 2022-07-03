"""
3.1.1.3 LAB: Catch me if you can!
https://edube.org/learn/pcpp1-4-gui-programming/lab-catch-me-if-you-can
Write a simple game - an infinite game which humans cannot win. Here are the rules:
    the game goes on between TkInter and the user (probably you)
    TkInter opens a 500x500 pixel window and places a button saying "Catch me!" in the top-left corner of the window;
    if the user moves the mouse cursor over the button, the button immediately jumps to another location inside the
    window; you have to assure that the new location is distant enough to prevent the user from making an instant click,
    the button must not cross the window's boundaries during the jump!
Use the place() method to move the button, and the bind() method to assign your own callback.
"""
import tkinter as tk
import random


def terminate():
    window.destroy()


def run(*args):
    current_x = button.place_info()['x']
    current_y = button.place_info()['y']
    new_x = random.randint(0, 410)
    while abs(int(current_x) - new_x) < 150:
        new_x = random.randint(0, 410)
    new_y = random.randint(0, 470)
    while abs(int(current_y) - new_y) < 100:
        new_y = random.randint(0, 410)
    button.place(x=new_x, y=new_y)


window = tk.Tk()
window.geometry("500x500")
window.resizable(width=False, height=False)
button = tk.Button(window, text="Catch me!", command=terminate)
button.place(x=410, y=470)
button.bind("<Enter>", run)
window.mainloop()
