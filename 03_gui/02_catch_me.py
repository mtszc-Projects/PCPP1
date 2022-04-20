"""
3.1.1.3 LAB: Catch me if you can!
https://edube.org/learn/pcpp1-4-gui-programming/lab-catch-me-if-you-can
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
