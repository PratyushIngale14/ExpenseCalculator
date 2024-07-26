import tkinter as tk
from tkinter import messagebox

class ExpenseCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Calculator")
        
    
        self.total_expense = 0.0

        
        self.create_widgets()

    def create_widgets(self):
        # Calculator Frame
        calc_frame = tk.Frame(self.root, padx=10, pady=10)
        calc_frame.grid(row=0, column=0, padx=10, pady=10)

        self.expression = ""
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(calc_frame, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        button_frame = tk.Frame(calc_frame, width=400, height=450, bg="grey")
        button_frame.pack()

        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '-',
            '1', '2', '3', '+', '=',
            '0', '.', 'Add Expense'
        ]

        row_val = 0
        col_val = 0
        for button in buttons:
            if button == 'Add Expense':
                tk.Button(button_frame, text=button, fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
                          command=lambda: self.add_expense()).grid(row=row_val, column=col_val, columnspan=2)
            else:
                tk.Button(button_frame, text=button, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                          command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

        # Expense Description Frame
        description_frame = tk.Frame(self.root, padx=10, pady=10)
        description_frame.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(description_frame, text="Expense Description:", font=('arial', 14)).grid(row=0, column=0, padx=5, pady=5)
        self.description_text = tk.Entry(description_frame, font=('arial', 14), width=40)
        self.description_text.grid(row=0, column=1, padx=5, pady=5)

        # Expense Tracker Frame
        tracker_frame = tk.Frame(self.root, padx=10, pady=10)
        tracker_frame.grid(row=2, column=0, padx=10, pady=10)

        self.expense_list = tk.Listbox(tracker_frame, height=10, width=50, font=('arial', 12))
        self.expense_list.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(tracker_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.expense_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.expense_list.yview)

        self.total_expense_label = tk.Label(self.root, text="Total Expense: $0.00", font=('arial', 18, 'bold'))
        self.total_expense_label.grid(row=3, column=0, padx=10, pady=10)

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
            self.input_text.set("")
        elif button == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("error")
                self.expression = ""
        else:
            self.expression += str(button)
            self.input_text.set(self.expression)

    def add_expense(self):
        try:
            expense = float(self.expression)
            description = self.description_text.get()
            if not description:
                raise ValueError("Description cannot be empty.")
            self.total_expense += expense
            self.expense_list.insert(tk.END, f"{description}: ${expense:.2f}")
            self.total_expense_label.config(text=f"Total Expense: ${self.total_expense:.2f}")
            self.expression = ""
            self.input_text.set("")
            self.description_text.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseCalculator(root)
    root.mainloop()
