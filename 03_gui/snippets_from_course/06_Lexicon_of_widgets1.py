"""
Below code snippets are taken from course content.
"""
# TODO: example 1 (Button widget)
# import tkinter as tk
#
#
# def switch():
#     if button_1.cget('state') == tk.DISABLED:
#         button_1.config(state=tk.NORMAL)
#         button_1.flash()
#     else:
#         button_1.flash()
#         button_1.config(state=tk.DISABLED)
#
#
# def mouseover(ev):
#     button_1['bg'] = 'green'
#
#
# def mouseout(ev):
#     button_1['bg'] = 'red'
#
#
# window = tk.Tk()
# button_1 = tk.Button(window, text="Enabled", bg="red")
# button_1.bind("<Enter>", mouseover)
# button_1.bind("<Leave>", mouseout)
# button_1.pack()
# button_2 = tk.Button(window, text="Enable/Disable", command=switch)
# button_2.pack()
# window.mainloop()

# TODO: example 2 (Checkbutton method)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def count():
#     global counter
#     counter += 1
#
#
# def show():
#     messagebox.showinfo("", "counter=" + str(counter) + ",state=" + str(switch.get()))
#
#
# window = tk.Tk()
# switch = tk.IntVar()
# counter = 0
# button = tk.Button(window, text="Show", command=show)
# button.pack()
# checkbutton = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
# checkbutton.pack()
# window.mainloop()

# TODO: example 3 (invoke() method - no code provided)

# TODO: example 4 (Radiobutton)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def show():
#     messagebox.showinfo("", "radio_1=" + str(radio_1_var.get()) +
#                         ",radio_2=" + str(radio_2_var.get()))
#
#
# def command_1():
#     radio_2_var.set(radio_1_var.get())
#
#
# def command_2():
#     radio_1_var.set(radio_2_var.get())
#
#
# window = tk.Tk()
# button = tk.Button(window, text="Show", command=show)
# button.pack()
# radio_1_var = tk.IntVar()
# radio_1_1 = tk.Radiobutton(window, text="pizza", variable=radio_1_var, value=1, command=command_1)
# radio_1_1.select()
# radio_1_1.pack()
# radio_1_2 = tk.Radiobutton(window, text="clams", variable=radio_1_var, value=2, command=command_1)
# radio_1_2.pack()
# radio_2_var = tk.IntVar()
# radio_2_1 = tk.Radiobutton(window, text="FR", variable=radio_2_var, value=2, command=command_2)
# radio_2_1.pack()
# radio_2_2 = tk.Radiobutton(window, text="IT", variable=radio_2_var, value=1, command=command_2)
# radio_2_2.select()
# radio_2_2.pack()
# window.mainloop()
