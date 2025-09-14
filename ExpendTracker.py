class Expense():
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

class Expense_Tracker():
    def __init__(self, balance):
        self.expenses = []
        self.balance = balance
        self.initial_balance = balance


    def add_expense(self, expense):
        self.expenses.append(expense)
        self.balance -= expense.amount

    def remove_expense(self, index):
        if 0<= index <len(self.expenses):
            removed = self.expenses.pop(index)
            self.balance += removed.amount
            print("Expense removed!")
        else:
            print("Invalid expense inex.")

    def view_expense(self):
        if len(self.expenses) == 0:
            print("No expenses found!")
        else:
            print("*** Expense List ***")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Category: {expense.category}, Description: {expense.description}, Amount: {expense.amount:,}T")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: {total:,}T")


def main():
    tracker = Expense_Tracker()

    while True:
        print("Expense Tracker Menu:")
        print("1.Add expense")
        print("2.Remove expense")
        print("3.view expense")
        print("4.Total expense")
        print("5.Exit")

        choice = input("\nEnter your choice 1-5: ")
        if choice == "1":
            date = input("Enter the date: ")
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            expense = Expense(date, category, description, amount)
            tracker.add_expense(expense)
            print("\nExpense added seccessfully")

        elif choice == "2":
            index = int(input("Enter the expense index to remove: ")) - 1
            tracker.remove_expense(index)

        elif choice == "3":
            tracker.view_expense()

        elif choice == "4":
            tracker.total_expenses()

        elif choice == "5":
            print("\n*** Goodbye for Now ***")
            break

        else:
            print("Invalidchoice, please try again!")

if __name__ == "__main__":
    main()


