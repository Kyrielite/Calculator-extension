import tkinter as tk
import math


root = tk.Tk()
root.title("Simple Calculator")

calculator = tk.Entry(root, bg="lavender", width=35, borderwidth=15)
calculator.grid(row=0, column=0, columnspan=4, padx=20, pady=10)

def button_click(number):
    """This function was borrowed with some modification,
    but this is my own documentation.
    Source code: https://bit.ly/2A63vB6
    
    This function allows the number the was pressed to appear in the text box.

    Parameters
    -----------
    number : int
        The corresponding number that has been pressed

    Returns
    -------
    returns str
        The number that was pressed will appear in the text box."""

    current = calculator.get()
    calculator.delete(0, tk.END)
    calculator.insert(0, str(current) + str(number))


def button_clear():
    """This function was borrowed with some modification,
    but this is my own documentation.
    Source code: https://bit.ly/2A63vB6

    This function allows the calculator to clear the number inside the text box.

    Parameters
    -----------
    number: int or float
        The number shown in the text box.

    Returns
    -------
    returns a blank text box
        The number previously shown in the text box will disappear.
    """

    calculator.delete(0, tk.END)


def button_add():
    """This function was borrowed with some modification,
    but this is my own documentation.
    Source code: https://bit.ly/2A63vB6

    This function allows two numbers to be added together.

    Parameters
    ----------
    number : float
        The first number will be stored

    Returns
    -------
    returns a blank text box
        The first number will be stored as a global variable to be used later
        and will disappear so that the user can enter the second number
        that will be later added with the first number"""

    first_number = calculator.get()
    global f_num
    global number
    number = "addition"
    f_num = float(first_number)
    calculator.delete(0, tk.END)


def button_subtract():
    """This function was borrowed with some modification,
    but this is my own documentation.
    Source code: https://bit.ly/2A63vB6

    This function allows the second number to be subtracted from the first number.

    Parameters
    ----------
    number : float

    Returns
    -------
    returns a blank text box.
        The first number will be stored as a global variable to be used later
        and will disappear so that the user can enter the second number
        so that the second number can be subtracted from the first number."""

    first_number = calculator.get()
    global f_num
    global number
    number = "subtraction"
    f_num = float(first_number)
    calculator.delete(0, tk.END)


def button_multiply():
    """This function was borrowed with some modification,
    but this is my own documentation.
    Source code: https://bit.ly/2A63vB6

    This function allows the second number to be multiplied with the first number.

    Parameters
    ----------
    number : float

    Returns
    -------
    returns a blank text box.
        The first number will be stored as a global variable to be used later
        and will disappear so that the user can enter the second number
        that will be later multplied with the first number """

    first_number = calculator.get()
    global f_num
    global number
    number = "multiplication"
    f_num = float(first_number)
    calculator.delete(0, tk.END)


def button_divide():
    """This function was borrowed with some modification,
    but this is my own documentation.
    Source code: https://bit.ly/2A63vB6

    This function allows the first number to be divided by the second number.

    Parameters
    ----------
    number : float

    Returns
    -------
    returns a blank text box.
        The first number will be stored as a global variable to be used later
        and will disappear so that the user can enter the second number
        so that the first number can be divided by the second number."""

    first_number = calculator.get()
    global f_num
    global number
    number = "division"
    f_num = float(first_number)
    calculator.delete(0, tk.END)


def button_equal():
    """This function was borrowed with some modification,
    but this is my own documentation.
    Source code: https://bit.ly/2A63vB6

    This function will carry out the math operation between two numbers.

    Parameters
    ----------
    f_num : float
    second_number : float
        These are the two numbers that the calculator will use to
        execute a math operation.

    Returns
    -------
    returns : float
        The math equation will execute and the result of it will appear
        in the text box."""

    second_number = calculator.get()
    calculator.delete(0, tk.END)

    if number == "addition":
        calculator.insert(0, f_num + float(second_number))

    if number == "subtraction":
        calculator.insert(0, f_num - float(second_number))

    if number == "multiplication":
        calculator.insert(0, f_num * float(second_number))

    if number == "division":
        calculator.insert(0, f_num / float(second_number))

    if number == "squared y":
        calculator.insert(0, f_num ** float(second_number))


def button_square_root():
    """This is my original funciton.
    This function gives the user the square root of the inputted number.

    Parameters
    ----------
    number : float

    Returns
    -------
    returns : float
        The result of a number that has been square rooted."""

    first_number = calculator.get()
    f_num = float(first_number)
    calculator.delete(0, tk.END)
    calculator.insert(0, math.sqrt(f_num))


def button_squared():
    """This is my original function.
    This function gives the user the square of the inputted number.

    Parameters
    ----------
    number : float

    Returns
    -------
    returns : float
        The result of a number that has been squared by 2."""
    first_number = calculator.get()
    global f_num
    f_num = float(first_number)
    calculator.delete(0, tk.END)
    calculator.insert(0, f_num ** 2)


def button_squared_y():
    """This is my original function.
    This function allows the first number to be squared by the second number.

    Parameters
    ----------
    number : float

    Returns
    -------
    returns a blank text box.
        The first number will be stored as a global variable to be used later
        and will disappear so that the user can enter the second number
        that will be later used to square the first number."""

    first_number = calculator.get()
    global f_num
    global number
    number = "squared y"
    f_num = float(first_number)
    calculator.delete(0, tk.END)

# This was also something that I added to improve the functionality of the calculator.
# This allows the buttons for the calculator to reconfigure its placement relative
# to how one stretches the calculator vertically.
root.columnconfigure(0, weight=1, minsize=75)
root.columnconfigure(1, weight=1, minsize=75)
root.columnconfigure(2, weight=1, minsize=75)
root.columnconfigure(3, weight=1, minsize=75)
root.columnconfigure(4, weight=1, minsize=75)

# This was also something I added that allows the buttons for the calculator
# to reconfigure its placement relative to how one stretches the calculator
# horizontally.
root.rowconfigure(1, weight=1, minsize=75)
root.rowconfigure(2, weight=1, minsize=75)
root.rowconfigure(3, weight=1, minsize=75)
root.rowconfigure(4, weight=1, minsize=75)


# This is external code, but I have modified some parts to it.
# Source code: https://bit.ly/2A63vB6
# This is to create the buttons on the calculator and each button's qualities.
button_1 = tk.Button(root, text="1", bg="light blue",
                     padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", bg="light blue",
                     padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", bg="light blue",
                     padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", bg="light blue",
                     padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", bg="light blue",
                     padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", bg="light blue",
                     padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", bg="light blue",
                     padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", bg="light blue",
                     padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", bg="light blue",
                     padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", bg="light blue",
                     padx=40, pady=20, command=lambda: button_click(0))

button_equal = tk.Button(root, text="=", bg="deep sky blue",
                         padx=40, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", bg="deep sky blue",
                         padx=29, pady=20, command=button_clear)

button_add = tk.Button(root, text="+", bg="turquoise",
                       padx=90, pady=20, command=button_add)
button_subtract = tk.Button(root, text="-", bg="turquoise",
                            padx=40, pady=20, command=button_subtract)
button_multiply = tk.Button(root, text="*", bg="turquoise",
                            padx=40, pady=20, command=button_multiply)
button_divide = tk.Button(root, text="/", bg="turquoise",
                          padx=40, pady=20, command=button_divide)

button_sqrt = tk.Button(root, text="√", bg="light slate blue",
                        padx=40, pady=20, command=button_square_root)
button_squared = tk.Button(root, text="x²", bg="light slate blue",
                           padx=40, pady=20, command=button_squared)
button_squared_y = tk.Button(root, text="x^y", bg="light slate blue",
                             padx=35, pady=20, command=button_squared_y)


# This is external code, but I have modified some parts to it.
# Source code: https://bit.ly/2A63vB6
# This is to have the buttons that was created earlier show up onto the calculator
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_add.grid(row=4, column=3, columnspan=2)
button_subtract.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=3, column=3)

button_sqrt.grid(row=1, column=4)
button_squared.grid(row=2, column=4)
button_squared_y.grid(row=3, column=4)


root.mainloop()
