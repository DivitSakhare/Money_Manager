import tkinter as tk
from tkinter import messagebox

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("400x500")  # Set the window size

        # Center the window on the screen
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        position_right = int(self.root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.root.winfo_screenheight() / 2 - window_height / 2)
        self.root.geometry("+{}+{}".format(position_right, position_down))

        # Configure the root window background color
        self.root.configure(bg="#ECECEC")

        # Create and configure the labels and entry fields for income
        self.label_income_name = tk.Label(root, text="Income Name:", bg="#ECECEC")
        self.label_income_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_income_name = tk.Entry(root)
        self.entry_income_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_income = tk.Label(root, text="Income Amount:", bg="#ECECEC")
        self.label_income.grid(row=1, column=0, padx=5, pady=5)
        self.entry_income = tk.Entry(root)
        self.entry_income.grid(row=1, column=1, padx=5, pady=5)

        # Create and configure the labels and entry fields for expenses
        self.label_expense_name = tk.Label(root, text="Expense Name:", bg="#ECECEC")
        self.label_expense_name.grid(row=2, column=0, padx=5, pady=5)
        self.entry_expense_name = tk.Entry(root)
        self.entry_expense_name.grid(row=2, column=1, padx=5, pady=5)

        self.label_expense_amount = tk.Label(root, text="Expense Amount:", bg="#ECECEC")
        self.label_expense_amount.grid(row=3, column=0, padx=5, pady=5)
        self.entry_expense_amount = tk.Entry(root)
        self.entry_expense_amount.grid(row=3, column=1, padx=5, pady=5)

        # Create a label for displaying the balance
        self.label_balance = tk.Label(root, text="Balance: $0", bg="#ECECEC")
        self.label_balance.grid(row=4, column=1, padx=5, pady=5)

        # Create the buttons for adding income and expenses
        self.add_income_button = tk.Button(root, text="Add Income", command=self.add_income)
        self.add_income_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.add_expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_expense_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        # Create a listbox to display the expenses
        self.expenses_listbox = tk.Listbox(root)
        self.expenses_listbox.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        # Create the button for showing the report
        self.report_button = tk.Button(root, text="Show Report", command=self.show_report)
        self.report_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        # Configure the listbox and balance label font and colors
        self.expenses_listbox.configure(font=("Arial", 10), bg="#F5F5F5", selectbackground="#ECECEC")
        self.label_balance.configure(font=("Arial", 12, "bold"), fg="#008000")

        # Initialize variables for tracking income and expenses
        self.income = 0
        self.expenses = []
        self.balance = 0

    def add_income(self):
        name = self.entry_income_name.get()
        amount = self.entry_income.get()
        if name and amount:
            try:
                amount = float(amount)
                if amount > 0:
                    self.income += amount
                    self.balance += amount
                    self.expenses_listbox.insert(tk.END, f"{name}: ${amount}")
                    messagebox.showinfo("Success", "Income added successfully.")
                    self.entry_income_name.delete(0, tk.END)
                    self.entry_income.delete(0, tk.END)
                    self.update_balance()
                else:
                    messagebox.showwarning("Invalid Input", "Income amount must be a positive number.")
            except ValueError:
                messagebox.showwarning("Invalid Input", "Please enter a valid number for income.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter both income name and amount.")

    def add_expense(self):
        name = self.entry_expense_name.get()
        amount = self.entry_expense_amount.get()
        if name and amount:
            try:
                amount = float(amount)
                if amount > 0:
                    expense = {"name": name, "amount": amount}
                    self.expenses.append(expense)
                    self.expenses_listbox.insert(tk.END, f"{name}: ${amount}")
                    self.balance -= amount
                    messagebox.showinfo("Success", "Expense added successfully.")
                    self.entry_expense_name.delete(0, tk.END)
                    self.entry_expense_amount.delete(0, tk.END)
                    self.update_balance()
                else:
                    messagebox.showwarning("Invalid Input", "Expense amount must be a positive number.")
            except ValueError:
                messagebox.showwarning("Invalid Input", "Please enter a valid number for the expense amount.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter both expense name and amount.")

    def show_report(self):
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        report = f"Income:\n{self.entry_income_name.get()}: ${self.income}\n\nExpenses:\n"
        for expense in self.expenses:
            report += f"{expense['name']}: ${expense['amount']}\n"
        report += f"\nTotal Expenses: ${total_expenses}\nBalance: ${self.balance}"
        messagebox.showinfo("Expense Report", report)

    def update_balance(self):
        self.label_balance.config(text=f"Balance: ${self.balance}")

# Create the main window
root = tk.Tk()

# Create an instance of the ExpenseTracker class
expense_tracker = ExpenseTracker(root)

# Start the Tkinter event loop
root.mainloop()
