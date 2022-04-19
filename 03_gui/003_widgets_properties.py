"""
Below code snippets are taken from course content.
"""
# TODO 1st example
# import tkinter as tk
#
#
# def on_off():
#     global button
#     state = button["text"]
#     if state == "ON":
#         state = "OFF"
#     else:
#         state = "ON"
#     button["text"] = state
#
#
# window = tk.Tk()
# button = tk.Button(window, text="OFF", command=on_off)
# button.place(x=50, y=100, width=100)
# window.mainloop()

# TODO 2st example
# import tkinter as tk
#
#
# def on_off():
#     global button
#     state = button.cget("text")
#     if state == "ON":
#         state = "OFF"
#     else:
#         state = "ON"
#     button.config(text=state)
#
#
# window = tk.Tk()
# button = tk.Button(window, text="OFF", command=on_off)
# button.place(x=50, y=100, width=100)
# window.mainloop()

# TODO 3rd example
# import tkinter as tk
#
#
# window = tk.Tk()
# label_1 = tk.Label(window, text="Quick brown fox jumps over the lazy dog")
# label_1.grid(column=0, row=0)
# label_2 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", "12"))
# label_2.grid(column=0, row=1)
# label_3 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Arial", "16", "bold"))
# label_3.grid(column=0, row=2)
# window.mainloop()

# TODO 4th example
# import tkinter as tk
#
#
# window = tk.Tk()
# button_1 = tk.Button(window, text="Ordinary button");
# button_1.pack()
# button_2 = tk.Button(window, text="Exceptional button")
# button_2.pack()
# button_2["borderwidth"] = 10
# button_2["highlightthickness"] = 10
# button_2["padx"] = 10
# button_2["pady"] = 5
# button_2["underline"] = 1
# window.mainloop()

# TODO 5th example
# import tkinter as tk
#
# window = tk.Tk()
# button_1 = tk.Button(window, text="Ordinary button")
# button_1.pack()
# button_2 = tk.Button(window, text="Colorful button")
# button_2.pack()
# button_2.config(bg="#000000")
# button_2.config(fg="yellow")
# button_2.config(activeforeground="#FF0000")
# button_2.config(activebackground="green")
# window.mainloop()

# TODO 6th example
# import tkinter as tk
#
# window = tk.Tk()
# button_1 = tk.Button(window, text="Regular button")
# button_1["anchor"] = 'e'
# button_1["width"] = 20  # pixels!
# button_1.pack()
# button_2 = tk.Button(window, text="Another button")
# button_2["anchor"] = 'sw'
# button_2["width"] = 20
# button_2["height"] = 3  # rows
# button_2.pack()
# window.mainloop()

# TODO 7th example
# import tkinter as tk
#
# window = tk.Tk()
# label_1 = tk.Label(window, height=3, text="arrow", cursor="arrow")
# label_1.pack()
# label_2 = tk.Label(window, height=3, text="clock", cursor="clock")
# label_2.pack()
# label_3 = tk.Label(window, height=3, text="heart", cursor="heart")
# label_3.pack()
# window.mainloop()
