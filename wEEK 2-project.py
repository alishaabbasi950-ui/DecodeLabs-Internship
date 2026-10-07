import json

# File where expenses will be saved
FILE_NAME = "expenses.json"


# Function to take and check expense
def get_expense():
    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Please enter an amount greater than 0.")
            else:
                return amount

        except ValueError:
            print("Invalid input. Please enter a number.")


# Load old expenses from file
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Main program
def main():

    expenses = load_expenses()

    total = 0

    print("================================")
    print("       EXPENSE TRACKER")
    print("================================")

    print("Enter your expenses.")
    print("Type 'quit' when you are finished.")
    print()

    while True:

        user_input = input("Expense: ")

        # Stop the program
        if user_input.lower() == "quit":
            break

        try:
            expense = float(user_input)

            if expense <= 0:
                print("Please enter a positive number.")
                continue

            # Accumulator
            total = total + expense

            # Save expense
            expenses.append(expense)
            save_expenses(expenses)

            print("Expense added successfully.")
            print("Running total: $", format(total, ".2f"))
            print()

        except ValueError:
            print("Invalid input. Please enter a number.")
            print()


    print("================================")
    print("       EXPENSE SUMMARY")
    print("================================")

    print("Total expenses: $", format(total, ".2f"))
    print("Number of transactions:", len(expenses))

    print("Thank you for using Expense Tracker!")


# Start program
if __name__ == "__main__":
    main()