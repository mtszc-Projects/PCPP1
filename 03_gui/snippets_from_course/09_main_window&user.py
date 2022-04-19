"""
Below code snippets are taken from course content.
"""
# TODO: example 1 (title change at runtime)
# import tkinter as tk
#
#
# def click(*args):
#     global counter
#     if counter > 0:
#         counter -= 1
#     window.title(str(counter))
#
#
# counter = 10
# window = tk.Tk()
# window.title(str(counter))
# window.bind("<Button-1>", click)
# window.mainloop()

# TODO: example 2 (icon change)
# import tkinter as tk
#
# window = tk.Tk()
# window.title('Icon?')
# window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='logo.png'))
# window.bind("&lt;Button-1&gt;", lambda e: window.destroy())
# window.mainloop()

# TODO: example 3 (geometry() -> changing windows default size)
# import tkinter as tk
#
#
# def click(*args):
#     global size, grows
#     if grows:
#         size += 50
#         if size >= 500:
#             grows = False
#     else:
#         size -= 50
#         if size <= 100:
#             grows = True
#     window.geometry(str(size) + "x" + str(size))
#
#
# size = 100
# grows = True
# window = tk.Tk()
# window.geometry("100x100")
# window.bind("&lt;Button-1&gt;", click)
# window.mainloop()

# TODO: example 4 (minsize())
# import tkinter as tk
#
# window = tk.Tk()
# window.minsize(width=250, height=200)
# window.geometry("500x500")
# window.mainloop()

# TODO: example 5 (maxsize())
# import tkinter as tk
#
# window = tk.Tk()
# window.maxsize(width=500, height=300)
# window.geometry("200x200")
# window.mainloop()

# TODO: example 6 (resizable())
# import tkinter as tk
#
# window = tk.Tk()
# window.resizable(width=False, height=False)
# window.geometry("400x200")
# window.mainloop()

# TODO: example 7 (protocol(), exiting program)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def really():
#     if messagebox.askyesno("?", "Wilt thou be gone?"):
#         window.destroy()
#
#
# window = tk.Tk()
# window.protocol("WM_DELETE_WINDOW", really)
# window.mainloop()

# TODO: example 8 (messagebox -> askyesno)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def question():
#     answer = messagebox.askyesno("?", "To be or not to be?")
#     print(answer)
#
#
# window = tk.Tk()
# button = tk.Button(window, text="Ask the question!", command=question)
# button.pack()
# window.mainloop()

# TODO: example 9 (messagebox -> askokcancel)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def question():
#     answer = messagebox.askokcancel("?", "I'm going to format your hard drive")
#     print(answer)
#
#
# window = tk.Tk()
# button = tk.Button(window, text="What are your plans?", command=question)
# button.pack()
# window.mainloop()

# TODO: example 10 (messagebox -> askretrycancel)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def question():
#     answer = messagebox.askretrycancel("?", "I'm going to format your hard drive")
#     print(answer)
#
#
# window = tk.Tk()
# button = tk.Button(window, text="What are your plans?", command=question)
# button.pack()
# window.mainloop()

# TODO: example 11 (messagebox -> askquestion)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def question():
#     answer = messagebox.askquestion("?", "I'm going to format your hard drive")
#     print(answer)
#
#
# window = tk.Tk()
# button = tk.Button(window, text="What are your plans?", command=question)
# button.pack()
# window.mainloop()

# TODO: example 12 (messagebox -> showerror)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def question():
#     answer = messagebox.showerror("!", "Your code does nothing!")
#     print(answer)
#
#
# window = tk.Tk()
# button = tk.Button(window, text="Alarming message", command=question)
# button.pack()
# window.mainloop()

# TODO: example 13 (messagebox -> showwarning)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def question():
#     answer = messagebox.showwarning("Be careful!", "Big Brother is watching you!")
#     print(answer)
#
#
# window = tk.Tk()
# button = tk.Button(window, text="What's going on?", command=question)
# button.pack()
# window.mainloop()
