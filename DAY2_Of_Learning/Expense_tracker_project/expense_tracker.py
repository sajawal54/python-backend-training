import csv
from pathlib import Path

file_path = Path(__file__).parent / "expenses.csv"


def show_menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")


def add_expense():

    title = input("Enter Title = ")
    category = input("Enter Category = ")

    try:
        amount = int(input("Enter Amount = "))

        with open(file_path, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([title, category, amount])

        print("Expense Added Successfully")

    except ValueError:
        print("Amount must be a number")


def view_expense():

    with open(file_path, "r") as file:

        reader = csv.reader(file)

        for row in reader:
            print(row)


def total_expense():

    total = 0

    with open(file_path, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            total += int(row[2])

    print("Total Expense =", total)


while True:

    show_menu()

    choice = input("Enter Choice = ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")