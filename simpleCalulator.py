'''
Create a user interface: Create a graphical user interface (GUI) using Python's Tkinter library. The interface should have buttons for numbers, arithmetic operators, and a display area for the result.

Implement the basic arithmetic operations: Your calculator should be able to perform addition, subtraction, multiplication, and division. Make sure to handle any errors that might occur, such as division by zero.

Add extra features: Once the basic calculator is working, add additional features such as the ability to calculate square roots, exponents, and trigonometric functions.

Test the calculator: Test the calculator thoroughly to ensure that it performs correctly for a wide range of inputs. Make sure that all the buttons and operations are working as intended.

Document your code: Write comments in your code to explain how it works and what each section does. This will make it easier for others to understand and modify your code in the future.

Submit your completed project: Once you have completed the calculator, submit it to me for review. Make sure to include any necessary files or documentation, and be prepared to explain how your calculator works and how you approached the project.
'''

import tkinter as tk

# Create a new GUI window
root = tk.Tk() # This creates a window
root.title("Calculator") # This gives

# Create a display widget for showing the calculator input/output
display = tk.Entry(root, width=25, justify="right", font=("Arial", 16))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define a function to update the display when a button is clicked
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

# Define functions for arithmetic operations
def button_add():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_subtract():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_multiply():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_divide():
    first_number = display.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    display.delete(0, tk.END)

def button_equal():
    second_number = display.get()
    display.delete(0, tk.END)

    if math_operation == "addition":
        display.insert(0, f_num + float(second_number))
    elif math_operation == "subtraction":
        display.insert(0, f_num - float(second_number))
    elif math_operation == "multiplication":
        display.insert(0, f_num * float(second_number))
    elif math_operation == "division":
        display.insert(0, f_num / float(second_number))

def button_clear():
    display.delete(0, tk.END)

# Create buttons for numbers and arithmetic operations
button_1 = tk.Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=30, pady=20, command=lambda: button_click(0))

button_add = tk.Button(root, text="+", padx=30, pady=20, command=button_add)
button_subtract = tk.Button(root, text="-", padx=30, pady=20, command=button_subtract)
button_multiply = tk.Button(root, text="*", padx=30, pady=20, command=button_multiply)
button_divide = tk.Button(root, text="/", padx=30, pady=20, command=button_divide)

button_equal = tk.Button(root, text="=", padx=64, pady=20, command=button_equal)
button_clear = tk.Button(root, text="C", padx=30, pady=20, command=button_clear)

# Add the buttons to the window
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

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=0, columnspan=4)

# Start the GUI event loop
root.mainloop()
