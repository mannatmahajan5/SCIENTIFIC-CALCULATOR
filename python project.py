#MANNAT'S CALCULATOR
import tkinter as tk
from math import sin, cos, tan, log, sqrt, pi, e

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Mannat's Calculator")
        self.root.configure(bg="light gray")  # Light background

        # Global variable to store the input expression
        self.expression = ""

        # Create the input field
        self.equation = tk.StringVar()
        input_field = tk.Entry(root, textvariable=self.equation, font=('Arial', 18), bd=10, insertwidth=4, width=24, borderwidth=5, relief="sunken")
        input_field.grid(row=0, column=0, columnspan=5, pady=10, padx=10)

        # Define button layout
        buttons = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'tan',
            '0', '.', '=', '+', 'log',
            'C', '(', ')', '^', 'sqrt',
            'Del', 'pi', 'e', '//', '%'
        ]

        # Map buttons to their functions
        button_functions = {
            'C': self.clear,
            'Del': self.backspace,
            'sin': lambda: self.scientific_func(sin),
            'cos': lambda: self.scientific_func(cos),
            'tan': lambda: self.scientific_func(tan),
            'log': lambda: self.scientific_func(log),
            'sqrt': lambda: self.scientific_func(sqrt),
            'pi': lambda: self.press(pi),
            'e': lambda: self.press(e),
            '^': lambda: self.press('^'),
            '=': self.evaluate,
            '//': lambda: self.press('//'),
            '%': lambda: self.press('%')
        }

        # Create button styles
        num_color = "light blue"
        operator_color = "light blue"
        special_color = "light blue"
        button_font = ('Arial', 16)

        # Create buttons and place them in the grid
        row, col = 1, 0
        for button in buttons:
            action = button_functions.get(button, lambda b=button: self.press(b))
            bg_color = (
                operator_color if button in ['+', '-', '*', '/', '=', 'sin', 'cos', 'tan', 'log', 'sqrt']
                else special_color if button in ['C', 'Del', 'pi', 'e', '^', '//', '%']
                else num_color
            )
            tk.Button(root, text=button, padx=20, pady=20, font=button_font, bg=bg_color, fg="black", command=action)\
                .grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Configure grid to make the buttons expand evenly
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def press(self, num):
        self.expression += str(num)
        self.equation.set(self.expression)

    def evaluate(self):
        try:
            # Replace ^ with ** for exponentiation
            self.expression = self.expression.replace('^', '**')
            result = str(eval(self.expression))
            self.equation.set(result)
            self.expression = result
        except Exception:
            self.equation.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.equation.set(self.expression)

    def scientific_func(self, func):
        try:
            # Evaluate the current expression for the function
            result = func(eval(self.expression))
            self.expression = str(result)
            self.equation.set(self.expression)
        except Exception:
            self.equation.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()




    
