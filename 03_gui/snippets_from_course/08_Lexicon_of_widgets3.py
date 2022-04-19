"""
Below code snippets are taken from course content.
"""
# TODO: example 1 (Entry widget)
# import tkinter as tk
#
#
# def digits_only(*args):
#     global last_string
#     string = text.get()
#     if string == '' or string.isdigit():  # Field's content is valid.
#         last_string = string
#     else:
#         text.set(last_string)
#
#
# last_string = ''
# window = tk.Tk()
# text = tk.StringVar()
# entry = tk.Entry(window, textvariable=text)
# text.set(last_string)
# text.trace('w', digits_only)
# entry.pack()
# entry.focus_set()
# window.mainloop()

# TODO: example 2 (MENU)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")
#
#
# window = tk.Tk()
#
# # main menu creation
# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
#
# # 1st main menu item: an empty (as far) submenu
# sub_menu_file = tk.Menu(main_menu)
# main_menu.add_cascade(label="File", menu=sub_menu_file)
#
# # 2nd main menu item: a simple callback
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app)
#
# window.mainloop()

# TODO: example 3 (MENU, add ALT+F, ALT+B as hot keys)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")
#
#
# window = tk.Tk()
#
# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu)
# # setting the hotkey to "Alt-F"
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# sub_menu_help = tk.Menu(main_menu)
# # setting the hotkey to "Alt-B"
# main_menu.add_command(label="About...", command=about_app, underline=1)
#
# window.mainloop()

# TODO: example 4 (MENU, add quit to File submenu)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")
#
#
# def are_you_sure():
#     if messagebox.askyesno("", "Are you sure you want to quit the App?"):
#         window.destroy()
#
#
# window = tk.Tk()
#
# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu)
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# # add the QUIT action to the submenu
# sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)
#
# window.mainloop()

# TODO: example 5 (MENU, disabling tear-off)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")
#
#
# def are_you_sure():
#     if messagebox.askyesno("", "Are you sure you want to quit the App?"):
#         window.destroy()
#
#
# window = tk.Tk()
#
# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# # we don't want the tear-off here
# sub_menu_file = tk.Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)
#
# window.mainloop()

# TODO: example 6 (MENU, add open to submenu File)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")
#
#
# def are_you_sure():
#     if messagebox.askyesno("", "Are you sure you want to quit the App?"):
#         window.destroy()
#
#
# def open_file():
#     messagebox.showinfo("Open doc", "We'll open a file here...")
#
#
# window = tk.Tk()
#
# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# # a new submenu item is here!
# sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
# sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)
#
# window.mainloop()

# TODO: example 7 (MENU, add_separator() in submenu)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")
#
#
# def are_you_sure():
#     if messagebox.askyesno("", "Are you sure you want to quit the App?"):
#         window.destroy()
#
#
# def open_file():
#     messagebox.showinfo("Open doc", "We'll open a file here...")
#
#
# window = tk.Tk()
#
# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
# # separator is here!
# sub_menu_file.add_separator()
# sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)
#
# window.mainloop()

# TODO: example 8 (MENU, add_cascade() in submenu)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")
#
#
# def are_you_sure():
#     if messagebox.askyesno("", "Are you sure you want to quit the App?"):
#         window.destroy()
#
#
# def open_file():
#     messagebox.showinfo("Open doc", "We'll open a file here...")
#
#
# window = tk.Tk()
#
# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
#
# sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
# sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)
#
# sub_menu_file.add_separator()
# sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)
#
# window.mainloop()


# TODO: example 9 (MENU, add_cascade() in submenu, add items)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")
#
#
# def are_you_sure():
#     if messagebox.askyesno("", "Are you sure you want to quit the App?"):
#         window.destroy()
#
#
# def open_file():
#     messagebox.showinfo("Open doc", "We'll open a file here...")
#
#
# window = tk.Tk()
#
# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
# sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
# sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)
#
# for i in range(8):
#     number = str(i + 1)
#     sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)
#
# sub_menu_file.add_separator()
# sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)
#
# window.mainloop()


# TODO: example 10 ((sub)menu items accessible by dedicated hot key)
# import tkinter as tk
# from tkinter import messagebox
#
#
# def about_app():
#     messagebox.showinfo("App", "The application\nthat does nothing")
#
#
# def are_you_sure(event=None):
#     if messagebox.askyesno("", "Are you sure you want to quit the App?"):
#         window.destroy()
#
#
# def open_file():
#     messagebox.showinfo("Open doc", "We'll open a file here...")
#
#
# window = tk.Tk()
#
# main_menu = tk.Menu(window)
# window.config(menu=main_menu)
# sub_menu_file = tk.Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
# sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
# sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
# sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)
#
# for i in range(8):
#     number = str(i + 1)
#     sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)
#
# sub_menu_file.add_separator()
# sub_menu_file.add_command(label="Quit", accelerator="Ctrl-Q",
#                           underline=0, command=are_you_sure)
# sub_menu_help = tk.Menu(main_menu)
# main_menu.add_command(label="About...", command=about_app, underline=1)
#
# window.bind_all("<Control-q>", are_you_sure)
# window.mainloop()


# TODO: example 11 (entryconfigure() to manipulate menus items)
# import tkinter as tk
#
#
# def on_off():
#     global accessible
#     if accessible == tk.DISABLED:
#         accessible = tk.ACTIVE
#     else:
#         accessible = tk.DISABLED
#     sub_menu.entryconfigure(1, state=accessible)
#
#
# accessible = tk.DISABLED
# window = tk.Tk()
# menu = tk.Menu(window)
# window.config(menu=menu)
# sub_menu = tk.Menu(menu, tearoff=0)
# menu.add_cascade(label="Menu", menu=sub_menu)
# sub_menu.add_command(label="On/Off", command=on_off)
# sub_menu.add_command(label="Switch", state=tk.DISABLED)
# window.mainloop()
