"""
Below code snippets are taken from course content.
"""

"""
Let tkinter speak!
"""
# import tkinter
# from tkinter import messagebox
#
#
# def click():
#     replay = messagebox.askquestion("Quit?", "Are you sure?")
#     if replay == 'yes':
#         skylight.destroy()
#
#
# skylight = tkinter.Tk()
# skylight.title("Skylight")
# button = tkinter.Button(skylight, text="Bye!", command=click)
# button.place(x=10, y=10)
# skylight.mainloop()

"""
Settling widgets in the window's interior
"""
# import tkinter as tk

# place()
# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.place(x=10, y=10, width=150)
# button_2.place(x=20, y=40)
# button_3.place(x=30, y=70, height=50)
# window.mainloop()

# grid()
# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.grid(row=0, column=0)
# button_2.grid(row=1, column=1)
# button_3.grid(row=2, column=0, columnspan=2)
# window.mainloop()

# pack() - first example
# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.pack()
# button_2.pack()
# button_3.pack()
# window.mainloop()

# pack() - second example
# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.pack(side=tk.RIGHT)
# button_2.pack()
# button_3.pack()
# window.mainloop()

# pack() - third example
# window = tk.Tk()
# button_1 = tk.Button(window, text="Button #1")
# button_2 = tk.Button(window, text="Button #2")
# button_3 = tk.Button(window, text="Button #3")
# button_1.pack(side=tk.RIGHT, fill=tk.Y)
# button_2.pack()
# button_3.pack()
# window.mainloop()

"""
Coloring your widgets
"""
# import tkinter as tk

# 1st example
# window = tk.Tk()
# button = tk.Button(window, text="Button #1", bg="red", fg="yellow")
# button.pack()
# window.mainloop()

# 2nd example
# window = tk.Tk()
# button = tk.Button(window, text="Button #1",
#                    bg="MediumPurple",
#                    fg="LightSalmon",
#                    activeforeground="LavenderBlush",
#                    activebackground="HotPink")
# button.pack()
# window.mainloop()

# 3rd example
# window = tk.Tk()
# button = tk.Button(window, text="Button #1",
#                    bg="#9370DB",
#                    fg="#FFA07A",
#                    activeforeground="#FFF0F5",
#                    activebackground="#FF69B4")
# button.pack()
# window.mainloop()
