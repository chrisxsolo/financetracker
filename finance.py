# File names to store data
expenses_file = "expenses.txt"
income_file = "income.txt"
available_money_file = "available_money.txt"

# Lists to store expenses and income
expenses = []
income = []

# Variable for available money
available_money = 0

# Function to load data from files
def load_data():
    try:
        with open(expenses_file, "r") as file:
            expenses.extend([float(line.strip()) for line in file.readlines()])
        
        with open(income_file, "r") as file:
            income.extend([float(line.strip()) for line in file.readlines()])

        with open(available_money_file, "r") as file:
            global available_money
            available_money = float(file.readline())
    except FileNotFoundError:
        pass

# Function to save data to files
def save_data():
    with open(expenses_file, "w") as file:
        file.write("\n".join(map(str, expenses)))
    
    with open(income_file, "w") as file:
        file.write("\n".join(map(str, income)))

    with open(available_money_file, "w") as file:
        file.write(str(available_money))

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

# Calculate remaining money after subtracting total spent and adding income
def calculate_remaining_money(total_spent):
    total_income = sum(income)
    remaining_money = total_income - total_spent + available_money

    display_finances(total_income, total_spent, remaining_money)

# Display the total income, total expenses, and remaining money to spend
def display_finances(total_income, total_expenses, remaining_money):
    print(f"\nTotal Freelance Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Money to Spend: ${remaining_money:.2f}")

# Load data from files
load_data()

# Menu
while True:
    print("\n1. Track Expenses")
    print("2. Show Available Money to Spend")
    print("3. Change Available Money to Spend")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        track_expenses()
    elif choice == "2":
        calculate_remaining_money(sum(expenses))
    elif choice == "3":
        new_available_money = float(input("Enter the new available money to spend: $"))
        available_money = new_available_money
        save_data()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option.")

