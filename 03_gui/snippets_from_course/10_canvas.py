"""
Below code snippets are taken from course content.
"""
# TODO: example 1 (polygonal chain)
# import tkinter as tk
#
#
# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
# canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380)
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

# TODO: example 2 (arrow heads)
# import tkinter as tk
#
# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
# canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380, arrow=tk.BOTH, fill='red', smooth=True, width=3)
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

# TODO: example 3 (create_rectangle())
# import tkinter as tk
#
# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='black')
# canvas.create_rectangle(200, 100, 300, 300, outline='white', width=5, fill='red')
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

# TODO: example 4 (create_polygon())
# import tkinter as tk
#
# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='black')
# canvas.create_polygon(20, 380, 200, 68, 380, 380, outline='red', width=5, fill='yellow')
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

# TODO: example 5 (create_oval())
# import tkinter as tk
#
# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='blue')
# canvas.create_oval(100, 100, 300, 200, outline='red', width=20, fill='white')
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

# TODO: example 5 (create_arc())
# import tkinter as tk
#
# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
# canvas.create_arc(10, 100, 380, 300, outline='red', width=5)
# canvas.create_arc(10, 100, 380, 300, outline='blue', width=5,
#                   style=tk.CHORD, start=90, fill='white')
# canvas.create_arc(10, 100, 380, 300, outline='green', width=5,
#                   style=tk.ARC, start=180, extent=180)
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

# TODO: example 6 (create_text())
# import tkinter as tk
#
# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='blue')
# canvas.create_text(200, 200, text="Mary\nhad\na\nlittle\nlamb",
#                    font=("Arial","40","bold"),
#                    justify=tk.CENTER,
#                    fill='white')
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

# TODO: example 7 (create_image())
# import tkinter as tk
#
# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
# image = tk.PhotoImage(file='logo.png')
# canvas.create_image(200, 200, image=image)
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()

# TODO: example 8 (JPG bitmap)
# import tkinter as tk
# import PIL
# from PIL import Image, ImageTk
#
# window = tk.Tk()
# canvas = tk.Canvas(window, width=400, height=400, bg='red')
# jpg = PIL.Image.open('logo.png')
# image = PIL.ImageTk.PhotoImage(jpg)
# canvas.create_image(200, 200, image=image)
# button = tk.Button(window, text="Quit", command=window.destroy)
# canvas.grid(row=0)
# button.grid(row=1)
# window.mainloop()
