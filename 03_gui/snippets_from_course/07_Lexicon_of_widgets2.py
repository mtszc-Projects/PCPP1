"""
Below code snippets are taken from course content.
"""
# TODO: example 1 (Label widget)
# import tkinter as tk
#
#
# def to_string(x):
#     return "Current counter\nvalue is:\n" + str(x)
#
#
# def plus():
#     global counter
#     counter += 1
#     text.set(to_string(counter))
#
#
# counter = 0
# window = tk.Tk()
# button = tk.Button(window, text="Go on!", command=plus)
# button.pack()
# text = tk.StringVar()
# label = tk.Label(window, textvariable=text, height=4)
# text.set(to_string(counter))
# label.pack()
# window.mainloop()

# TODO: example 2 (Message widget)
# import tkinter as tk
#
#
# def do_it_again():
#     text.set(text.get() + "and again...")
#
#
# window = tk.Tk()
# button = tk.Button(window, text="Go ahead!", command=do_it_again)
# button.pack()
# text = tk.StringVar()
# message = tk.Message(window, textvariable=text, width=400)
# text.set("You did it again... ")
# message.pack()
# window.mainloop()

# TODO: example 3 (Frame widget)
# import tkinter as tk
#
# window = tk.Tk()
#
# frame_1 = tk.Frame(window, width=200, height=100, bg='white')
# frame_2 = tk.Frame(window, width=200, height=100, bg='yellow')
#
# button_1_1 = tk.Button(frame_1, text="Button #1 inside Frame #1")
# button_1_2 = tk.Button(frame_1, text="Button #2 inside Frame #1")
# button_2_1 = tk.Button(frame_2, text="Button #1 inside Frame #2")
# button_2_2 = tk.Button(frame_2, text="Button #2 inside Frame #2")
#
# button_1_1.place(x=10, y=10)
# button_1_2.place(x=10, y=50)
# button_2_1.grid(column=0, row=0)
# button_2_2.grid(column=1, row=1)
#
# frame_1.pack()
# frame_2.pack()
#
# window.mainloop()

# TODO: example 4 (LabelFrame widget)
# import tkinter as tk
#
# window = tk.Tk()
# label_frame_1 = tk.LabelFrame(window, text="Frame #1",
#                               width=200, height=100, bg='white')
# label_frame_2 = tk.LabelFrame(window, text="Frame #2",
#                               labelanchor='se', width=200, height=100, bg='yellow')
#
# button_1_1 = tk.Button(label_frame_1, text="Button #1 inside Frame #1")
# button_1_2 = tk.Button(label_frame_1, text="Button #2 inside Frame #1")
# button_2_1 = tk.Button(label_frame_2, text="Button #1 inside Frame #2")
# button_2_2 = tk.Button(label_frame_2, text="Button #2 inside Frame #2")
#
# button_1_1.place(x=10, y=10)
# button_1_2.place(x=10, y=50)
# button_2_1.grid(column=0, row=0)
# button_2_2.grid(column=1, row=1)
#
# label_frame_1.pack()
# label_frame_2.pack()
# window.mainloop()
