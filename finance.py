# Lists to store expenses and income
expenses = []
income = []

# Function to track expenses
def track_expenses():
    total_spent = 0

    while True:
        expense = input("Enter expense amount (or 'done' to finish): ")
        if expense.lower() == "done":
            track_income()
            break

        try:
            expense_amount = float(expense)
            if expense_amount <= 0:
                print("Invalid expense amount. Please enter a valid number.")
                continue

            expenses.append(expense_amount)
            total_spent += expense_amount
            if total_spent >= 3000:
                track_income()
                break
        except ValueError:
            print("Invalid expense amount. Please enter a valid number.")

# Function to track income
def track_income():
    while True:
        income_earned = input("Enter income earned (or 'done' to finish): ")
        if income_earned.lower() == "done":
            display_finances()
            break

        try:
            income_amount = float(income_earned)
            if income_amount <= 0:
                print("Invalid income earned. Please enter a valid number.")
                continue

            income.append(income_amount)
        except ValueError:
            print("Invalid income earned. Please enter a valid number.")

# Display the tracked expenses and income, along with total money spent and total money earned
def display_finances():
    print("Expenses:")
    for expense in expenses:
        print(f"Amount: ${expense:.2f}")

    print("\nIncome:")
    for income_earned in income:
        print(f"Amount: ${income_earned:.2f}")

    total_spent = sum(expenses)
    total_earned = sum(income)
    print(f"\nTotal Money Spent: ${total_spent:.2f}")
    print(f"Total Money Earned: ${total_earned:.2f}")

# Track expenses
track_expenses()
