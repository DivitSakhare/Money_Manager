# Money_Manager

Introduction
This is a simple Expense Tracker application created using Python's Tkinter library. The Expense Tracker helps users manage their income and expenses, providing a user-friendly GUI to input financial data and generate reports. This README provides a detailed explanation of the code structure and functionality.

Prerequisites
Before running the Expense Tracker application, make sure you have Python installed on your system. Additionally, Tkinter, the built-in Python library for GUI development, should be available. Most Python installations include Tkinter by default.

Code Explanation
1. Main Application Class
   The core of the application is the ExpenseTracker class, which is responsible for creating the GUI and managing user interactions. It's initiated with the main window as an argument.
2. GUI Initialization
   The ExpenseTracker class sets up the main window's title, dimensions, and positions it at the center of the screen. It also configures the background color and creates labels, entry fields, buttons, and a listbox for user input and display.
3. Adding Income and Expenses
   Two methods, add_income and add_expense, are provided for adding income and expenses, respectively. These methods validate user input, ensuring that the name and amount are provided and that the amount is a valid positive number. The income or expense is then added to the appropriate list, and the balance is updated accordingly.
4. Displaying Reports
   The show_report method generates a financial report that displays the income, individual expenses, total expenses, and the current balance. This report is presented to the user in a message box.
5. Updating the Balance
   The update_balance method keeps the balance label on the GUI updated with the current balance.
6. Variable Initialization
   The application initializes three variables: income, expenses, and balance. These variables keep track of the user's financial data as they input income and expenses.
7. Application Initialization and Main Loop
   The code creates the main window using Tkinter, instantiates the ExpenseTracker class, and starts the Tkinter event loop, which handles user interactions and GUI updates.

Usage
1. Run the Python script containing the Expense Tracker code.
2. The application GUI will appear, allowing you to input income and expenses.
3. Click the "Add Income" button to add your income, providing the income name and amount.
4. Click the "Add Expense" button to add your expenses, providing the expense name and amount.
5. You can add multiple income and expense entries.
6. To view a financial report, click the "Show Report" button, and a message box will display the summary of your income, expenses, total expenses, and balance.

This README should help users understand the functionality of the Expense Tracker application and provide guidance on how to use and extend it for their specific requirements.
