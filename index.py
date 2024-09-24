import tkinter as tk
from math import sqrt

# Define button click event
def button_click(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + str(value))

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Function to calculate square root
def square_root():
    try:
        num = float(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(sqrt(num)))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Function to calculate power
def power():
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + "**")

# Create main window
window = tk.Tk()
window.title("Calculator")

# Display screen
display = tk.Entry(window, width=30, borderwidth=5, font=("Arial", 18))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    'C', '0', '=', '+', 
    '√', '^'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(window, text=button, width=9, height=3, command=calculate).grid(row=row, column=col, columnspan=2)
    elif button == 'C':
        tk.Button(window, text=button, width=9, height=3, command=clear_display).grid(row=row, column=col)
    elif button == '√':
        tk.Button(window, text=button, width=9, height=3, command=square_root).grid(row=row, column=col)
    elif button == '^':
        tk.Button(window, text=button, width=9, height=3, command=power).grid(row=row, column=col)
    else:
        tk.Button(window, text=button, width=9, height=3, command=lambda value=button: button_click(value)).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the GUI event loop
window.mainloop()
