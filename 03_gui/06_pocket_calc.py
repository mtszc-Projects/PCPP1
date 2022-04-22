"""
3.2.1.1 PROJECT: Pocket calculator
https://edube.org/learn/pcpp1-4-gui-programming/project-pocket-calculator
"""
import tkinter as tk


class PocketCalculator:
    current_value = 0.0
    standard_width = 4
    standard_height = 4
    addition = False
    subtraction = False
    multiplication = False
    division = False

    def button_press(self, value):
        entry_val = self.number_entry.get()
        if len(entry_val) < 10:
            entry_val += value
            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, entry_val)
        else:
            return

    @staticmethod
    def isfloat(str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def math_button_press(self, value):
        if self.isfloat(str(self.number_entry.get())):
            self.addition = False
            self.subtraction = False
            self.multiplication = False
            self.division = False
            self.current_value = float(self.entry_value.get())
            if value == "+":
                self.addition = True
            elif value == "-":
                self.subtraction = True
            elif value == "*":
                self.multiplication = True
            elif value == "/":
                self.division = True
            elif value == "/":
                self.subtraction = True
            elif value == "C":
                solution = ''
                self.number_entry.delete(0, "end")
                self.number_entry.insert(0, str(solution))
            else:
                solution = -1 * self.current_value
                if solution % 1 == 0.0:
                    solution = int(solution)
                self.number_entry.delete(0, "end")
                self.number_entry.insert(0, str(solution))
                return
            self.number_entry.delete(0, "end")
        else:
            if value == "C":
                solution = ''
                self.number_entry.delete(0, "end")
                self.number_entry.insert(0, str(solution))

    def equal_button_press(self):
        if self.addition or self.subtraction or self.multiplication or self.division:
            if self.addition:
                solution = float(f'{self.current_value + float(self.entry_value.get()):.3f}')
                if float(solution) % 1 == 0.0:
                    solution = int(solution)
            elif self.subtraction:
                solution = float(f'{self.current_value - float(self.entry_value.get()):.3f}')
                if float(solution) % 1 == 0.0:
                    solution = int(solution)
            elif self.multiplication:
                solution = float(f'{self.current_value * float(self.entry_value.get()):.3f}')
                if float(solution) % 1 == 0.0:
                    solution = int(solution)
            else:
                try:
                    solution = float(f'{self.current_value / float(self.entry_value.get()):.3f}')
                    if solution % 1 == 0.0:
                        solution = int(solution)
                except ZeroDivisionError:
                    solution = 'Error!'
            if len(str(solution)) > 10:
                solution = 'Error!'
            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, str(solution))

    def __init__(self, window):
        self.entry_value = tk.StringVar(window, value="")
        window.title("Pocket calculator")
        window.resizable(width=False, height=False)
        self.number_entry = tk.Entry(window, font="Helvetica 44 bold", justify='right', width=10,
                                     textvariable=self.entry_value)
        self.number_entry.grid(row=0, columnspan=5)
        # 1st Row
        self.button7 = tk.Button(window, text="7", width=self.standard_width,
                                 height=self.standard_height, command=lambda: self.button_press('7'))
        self.button7.grid(row=1, column=0)
        self.button8 = tk.Button(window, text="8", width=self.standard_width,
                                 height=self.standard_height, command=lambda: self.button_press('8'))
        self.button8.grid(row=1, column=1)
        self.button9 = tk.Button(window, text="9", width=self.standard_width,
                                 height=self.standard_height, command=lambda: self.button_press('9'))
        self.button9.grid(row=1, column=2)
        self.button_add = tk.Button(window, text="+", width=self.standard_width,
                                    height=self.standard_height, command=lambda: self.math_button_press('+'))
        self.button_add.grid(row=1, column=4)
        # 2nd Row
        self.button4 = tk.Button(window, text="4", width=self.standard_width,
                                 height=self.standard_height, command=lambda: self.button_press('4'))
        self.button4.grid(row=2, column=0)
        self.button5 = tk.Button(window, text="5", width=self.standard_width,
                                 height=self.standard_height, command=lambda: self.button_press('5'))
        self.button5.grid(row=2, column=1)
        self.button6 = tk.Button(window, text="6", width=self.standard_width,
                                 height=self.standard_height, command=lambda: self.button_press('6'))
        self.button6.grid(row=2, column=2)
        self.button_sub = tk.Button(window, text="-", width=self.standard_width,
                                    height=self.standard_height, command=lambda: self.math_button_press('-'))
        self.button_sub.grid(row=2, column=4)
        # 3rd Row
        self.button1 = tk.Button(window, text="1", width=self.standard_width,
                                 height=self.standard_height, command=lambda: self.button_press('1'))
        self.button1.grid(row=3, column=0)
        self.button2 = tk.Button(window, text="2", width=self.standard_width,
                                 height=self.standard_height, command=lambda: self.button_press('2'))
        self.button2.grid(row=3, column=1)
        self.button3 = tk.Button(window, text="3", width=self.standard_width,
                                 height=self.standard_height, command=lambda: self.button_press('3'))
        self.button3.grid(row=3, column=2)
        self.button_equal = tk.Button(window, text="=", width=6,
                                      height=self.standard_height, command=lambda: self.equal_button_press())
        self.button_equal.grid(row=3, column=3)
        self.button_mult = tk.Button(window, text="*", width=self.standard_width,
                                     height=self.standard_height, command=lambda: self.math_button_press('*'))
        self.button_mult.grid(row=3, column=4)
        # 4th Row
        self.button0 = tk.Button(window, text="0", width=self.standard_width,
                                 height=self.standard_height, command=lambda: self.button_press('0'))
        self.button0.grid(row=4, column=0)
        self.button_clear = tk.Button(window, text="C", width=self.standard_width,
                                      height=self.standard_height, command=lambda: self.math_button_press('C'))
        self.button_clear.grid(row=4, column=1)
        self.button_dot = tk.Button(window, text=".", width=self.standard_width,
                                    height=self.standard_height, command=lambda: self.button_press('.'))
        self.button_dot.grid(row=4, column=2)
        self.button_invert = tk.Button(window, text="+/-", width=6,
                                       height=self.standard_height, command=lambda: self.math_button_press('+/-'))
        self.button_invert.grid(row=4, column=3)
        self.button_div = tk.Button(window, text="/", width=self.standard_width,
                                    height=self.standard_height, command=lambda: self.math_button_press('/'))
        self.button_div.grid(row=4, column=4)


wnd = tk.Tk()
calc = PocketCalculator(wnd)
wnd.mainloop()
