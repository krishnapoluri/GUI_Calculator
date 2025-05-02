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
