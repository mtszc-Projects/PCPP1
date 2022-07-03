"""
3.1.1.4 LAB: The clicker
https://edube.org/learn/pcpp1-4-gui-programming/lab-the-clicker
We want you to write a simple but challenging game, which can help many people to improve their perception skills and
visual memory. We'll call the game The Clicker as clicking is what we expect from the player.
The Clicker's board consists of 25 buttons and each of the buttons contains a random number from range 1..999.
Note: each number is different!
Below the board there is a timer which initially shows 0. The timer starts when the user clicks the board for the first
time.
Here's how we imagine The Clicker's initial board state:
The Clicker - initial board's state
We expect the player to click all the buttons in the order imposed by the numbers - from the lowest to the highest one.
Additional rules say that:
    the properly clicked button changes the button's state to DISABLED (it greys the button out)
    the improperly clicked button shows no activity,
    the timer increases its value every second,
    when all the buttons are greyed out (i.e., the player has completed his/her task) the timer stops immediately.
This is how the board looks when the game is finished:
The Clicker - final board's state
Hint: consider using the <Button-1> event instead of setting the command button property - it may simplify your code.
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
