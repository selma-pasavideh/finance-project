class Expend():
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

class Expense_Tracker():
    def __init__(self):
        self.expenses = []


    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0<= index <len(self.expenses):
            del self.expenses[index]
            print("Expense removed!")
        else:
            print("Invalid expense inex.")

    def view_expense(self):
        if len(self.expenses) == 0:
            print("No expenses found!")
        else:
            print("*** Expense List ***")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Category: {expense.category}, Description: {expense.description}, Amount: {expense.amount:.2f}T")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: {total:.3f}T")


