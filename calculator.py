import tkinter as tk
import math

# Function to safely evaluate expressions
def calculate():
    try:
        expr = entry.get()
        expr = expr.replace("^", "**").replace("√", "math.sqrt")
        expr = expr.replace("sin", "math.sin(math.radians")
        expr = expr.replace("cos", "math.cos(math.radians")
        expr = expr.replace("tan", "math.tan(math.radians")
        expr = expr.replace("log", "math.log10")
        expr = expr.replace("ln", "math.log")
        # Balance parentheses for sin, cos, tan
        open_funcs = ["math.sin(", "math.cos(", "math.tan("]
        for func in open_funcs:
            if func in expr:
                expr += ")"
        result = eval(expr, {"math": math, "__builtins__": None})
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to add text to entry field
def press(key):
    entry.insert(tk.END, key)

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Advanced Calculator")
entry = tk.Entry(root, width=35, font=("Arial", 16), borderwidth=5, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Button layout
buttons = [
    ('7', '8', '9', '/', 'sqrt('),
    ('4', '5', '6', '*', 'log('),
    ('1', '2', '3', '-', 'ln('),
    ('0', '.', '^', '+', '√'),
    ('(', ')', 'sin(', 'cos(', 'tan('),
    ('Clear', '=', '', '', '')
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == '':
            continue
        elif text == 'Clear':
            btn = tk.Button(root, text=text, width=7, height=2, command=clear)
        elif text == '=':
            btn = tk.Button(root, text=text, width=7, height=2, command=calculate)
        else:
            btn = tk.Button(root, text=text, width=7, height=2, command=lambda t=text: press(t))
        btn.grid(row=i+1, column=j, padx=2, pady=2)

root.mainloop()

