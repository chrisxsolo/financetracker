# File names to store data
expenses_file = "expenses.txt"
income_file = "income.txt"

# Lists to store expenses and income
expenses = []
income = []

# Function to load data from files
def load_data():
    try:
        with open(expenses_file, "r") as file:
            expenses.extend([float(line.strip()) for line in file.readlines()])
        
        with open(income_file, "r") as file:
            income.extend([float(line.strip()) for line in file.readlines()])
    except FileNotFoundError:
        pass

# Function to save data to files
def save_data():
    with open(expenses_file, "w") as file:
        file.write("\n".join(map(str, expenses)))
    
    with open(income_file, "w") as file:
        file.write("\n".join(map(str, income)))

# Function to track expenses
def track_expenses():
    total_spent = sum(expenses)

    while True:
        expense = input("Enter expense amount (or 'done' to finish): ")
        if expense.lower() == "done":
            save_data()
            track_income()
            break

        try:
            expense_amount = float(expense)
            if expense_amount <= 0:
                print("Invalid expense amount. Please enter a valid number.")
                continue

            if total_spent + expense_amount > 1700:
                print("You have reached the spending limit of $1700 for this month.")
                break

            expenses.append(expense_amount)
            total_spent += expense_amount

        except ValueError:
            print("Invalid expense amount. Please enter a valid number.")

    calculate_remaining_money(total_spent)

# Function to track income
def track_income():
    while True:
        income_earned = input("Enter income earned (or 'done' to finish): ")
        if income_earned.lower() == "done":
            save_data()
            calculate_remaining_money(sum(expenses))
            break

        try:
            income_amount = float(income_earned)
            if income_amount <= 0:
                print("Invalid income earned. Please enter a valid number.")
                continue

            income.append(income_amount)
        except ValueError:
            print("Invalid income earned. Please enter a valid number.")

# Calculate remaining money after subtracting total spent from $1700
def calculate_remaining_money(total_spent):
    remaining_money = 1700 - total_spent

    display_finances(remaining_money)

# Display the tracked expenses and income, along with the remaining money
def display_finances(remaining_money):
    print("Expenses:")
    for expense in expenses:
        print(f"Amount: ${expense:.2f}")

    print("\nIncome:")
    for income_earned in income:
        print(f"Amount: ${income_earned:.2f}")

    print(f"\nRemaining Money: ${remaining_money:.2f}")

# Load data from files
load_data()

# Track expenses
track_expenses()
