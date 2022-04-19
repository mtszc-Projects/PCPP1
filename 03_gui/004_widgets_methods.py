"""
Below code snippets are taken from course content.
"""
# TODO 1st example
# import tkinter as tk
#
#
# def blink():
#     global is_white
#     if is_white:
#         color = 'black'
#     else:
#         color = 'white'
#     is_white = not is_white
#     frame.config(bg=color)
#     frame.after(500, blink)
#
#
# is_white = True
# window = tk.Tk()
# frame = tk.Frame(window, width=200, height=100, bg='white')
# frame.after(500, blink)
# frame.pack()
# window.mainloop()

# TODO 2st example
# import tkinter as tk
#
#
# def suicide():
#     frame.destroy()
#
#
# window = tk.Tk()
# frame = tk.Frame(window, width=200, height=100, bg='green')
# button = tk.Button(frame, text="I'm a frame's child")
# button.place(x=10, y=10)
# frame.after(5000, suicide)
# frame.pack()
# window.mainloop()

# TODO 3rd example
# import tkinter as tk
#
#
# def flip_focus():
#     if window.focus_get() is button_1:
#         button_2.focus_set()
#     else:
#         button_1.focus_set()
#     window.after(1000, flip_focus)
#
#
# window = tk.Tk()
# button_1 = tk.Button(window, text="First")
# button_1.pack()
# button_2 = tk.Button(window, text="Second")
# button_2.pack()
# window.after(1000, flip_focus)
# window.mainloop()
