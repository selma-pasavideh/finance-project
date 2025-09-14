class Expend():
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

class Expense_Tracke():
    def __init__(self):
        self.expenses = []