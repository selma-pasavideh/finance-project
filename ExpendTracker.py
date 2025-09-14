class Expend():
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

class Expense_Tracke():
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