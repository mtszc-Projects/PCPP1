"""
Below code snippets are taken from course content.
"""
# TODO 1st example
# import tkinter
# from tkinter import messagebox
#
#
# def clicked():
#     messagebox.showinfo("info", "some\ninfo")
#
#
# window = tkinter.Tk()
# button_1 = tkinter.Button(window, text="Show info", command=clicked)
# button_1.pack()
# button_2 = tkinter.Button(window, text="Quit", command=window.destroy)
# button_2.pack()
# window.mainloop()

# TODO 2st example
# import tkinter as tk
# from tkinter import messagebox
#
#
# def click():
#     tk.messagebox.showinfo("Click!", "I love clicks!")
#
#
# window = tk.Tk()
# label = tk.Label(window, text="Label")
# label.pack()
#
# button = tk.Button(window, text="Button", command=click)
# button.pack(fill=tk.X)
#
# frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
# frame.pack()
#
# window.mainloop()

# TODO 3rd example
# import tkinter as tk
# from tkinter import messagebox
#
#
# def click(event=None):
#     tk.messagebox.showinfo("Click!", "I love clicks!")
#
#
# window = tk.Tk()
# label = tk.Label(window, text="Label")
# label.bind("<Button-1>", click)   # Line I
# label.pack()
#
# button = tk.Button(window, text="Button", command=click)
# button.pack(fill=tk.X)
#
# frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
# frame.bind("<Button-1>", click)   # Line II
# frame.pack()
#
# window.mainloop()

# TODO 4th example
# import tkinter as tk
# from tkinter import messagebox
#
#
# def click(event=None):
#     if event is None:
#         tk.messagebox.showinfo("Click!", "I love clicks!")
#     else:
#         string = "x=" + str(event.x) + ",y=" + str(event.y) + \
#                  ",num=" + str(event.num) + ",type=" + event.type
#         tk.messagebox.showinfo("Click!", string)
#
#
# window = tk.Tk()
# label = tk.Label(window, text="Label")
# label.bind("<Button-1>", click)
# label.pack()
#
# button = tk.Button(window, text="Button", command=click)
# button.pack(fill=tk.X)
#
# frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
# frame.bind("<Button-1>", click)
# frame.pack()
#
# window.mainloop()

# TODO 5th example
# import tkinter as tk
# from tkinter import messagebox
#
#
# def on_off():
#     global switch
#     if switch:
#         button_2.config(command=lambda: None)
#         button_2.config(text="Gee!")
#     else:
#         button_2.config(command=peekaboo)
#         button_2.config(text="Peekaboo!")
#     switch = not switch
#
#
# def peekaboo():
#     messagebox.showinfo("", "PEEKABOO!")
#
#
# def do_nothing():
#     pass
#
#
# switch = True
# window = tk.Tk()
# button_1 = tk.Button(window, text="On/Off", command=on_off)
# button_1.pack()
# button_2 = tk.Button(window, text="Peekaboo!", command=peekaboo)
# button_2.pack()
# window.mainloop()

# TODO 6th example
# import tkinter as tk
#
#
# def on_off():
#     global switch
#     if switch:
#         label.unbind("<Button-1>")
#     else:
#         label.bind("<Button-1>", rhyme)
#     switch = not switch
#
#
# def rhyme(dummy):
#     global word_no, words
#     word_no += 1
#     label.config(text=words[word_no % len(words)])
#
#
# switch = True
# words = ["Old", "McDonald", "Had", "A", "Farm"]
# word_no = 0
# window = tk.Tk()
# button = tk.Button(window, text="On/Off", command=on_off)
# button.pack()
# label = tk.Label(window, text=words[0])
# label.bind("<Button-1>", rhyme)
# label.pack()
# window.mainloop()

# TODO 7th example
# import tkinter as tk
# from tkinter import messagebox
#
#
# def hello(dummy):
#     messagebox.showinfo("", "Hello!")
#
#
# window = tk.Tk()
# button = tk.Button(window, text="On/Off")
# button.pack()
# label = tk.Label(window, text="Label")
# label.pack()
# frame = tk.Frame(window, bg="yellow", width=100, height=20)
# frame.pack()
# window.bind_all("<Button-1>", hello)
# window.mainloop()
