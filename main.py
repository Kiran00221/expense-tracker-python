import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


def add_transaction():
    """Add income or expense entry."""
    t_type = input("Enter type (income/expense): ").lower()
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., food, travel, rent): ").capitalize()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, t_type, amount, category])

    print("Transaction added successfully!")


def view_transactions():
    """Display all transactions."""
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            print(f"\n{'Date':12} | {'Time':8} | {'Type':10} | {'Amount (₹)':12} | {'Category':10}")
            print("-" * 70)
            for row in reader:
                full_datetime, t_type, amount, category = row
                date_part, time_part = full_datetime.split(" ")
                print(f"{date_part:12} | {time_part:8} | {t_type:10} | ₹{float(amount):10.2f} | {category:10}")
    except FileNotFoundError:
        print("No transactions found yet.")


def show_summary():
    """Show total income, expenses, and balance."""
    income = 0
    expense = 0

    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == "income":
                    income += float(row[2])
                elif row[1] == "expense":
                    expense += float(row[2])
    except FileNotFoundError:
        print("No transactions found yet.")
        return

    print(f"\nTotal Income: ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Net Balance: ₹{income - expense}")


def main():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
