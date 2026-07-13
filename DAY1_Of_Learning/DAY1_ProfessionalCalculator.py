# Menu Screen
import math
def show_menu():
    print("\n" + "=" * 40)
    print("      PROFESSIONAL CALCULATOR")
    print("=" * 40)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Exit")

    print("=" * 40)



# Addition Function
def add():
     num1 = float(input("Enter First Number: "))
     num2 = float(input("Enter Second Number: "))

     result = num1 + num2

     print(f"\nResult = {result}")


# Subtraction Function
def subtract():
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    result = num1 - num2

    print(f"\nResult = {result}")

# Multiplication Function
def multiply():
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    result = num1 * num2

    print(f"\nResult = {result}")

# Division Function
def divide():
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if num2 == 0:
        print("Cannot divide by zero.")
        return

    result = num1 / num2

    print(f"\nResult = {result}")

# Power Function
def power():
    num1 = float(input("Enter Base Number: "))
    num2 = float(input("Enter Power: "))

    result = num1 ** num2

    print(f"\nResult = {result}")

# SquareRoot function
def square_root():
    number = float(input("Enter Number: "))

    if number < 0:
     print("Square root of a negative number is not possible.")
     return
    result = math.sqrt(number)
    print(f"\nSquare Root = {result}")

# Percentage Function
def percentage():
    total = float(input("Enter Total Value: "))
    percent = float(input("Enter Percentage: "))

    result = (percent / 100) * total

    print(f"\nResult = {result}")


while True:
    show_menu()

    choice = input("Enter your choice = ")

    if choice == "1":
         add()

    elif choice == "2":
         subtract()

    elif choice == "3":
         multiply()

    elif choice == "4":
         divide()

    elif choice == "5":
        power()
      
    elif choice == "6":
        square_root()

    elif choice == "7":
        percentage()

    elif choice == "8":
         print("Thank you for using the calculator.")
         break

    else:
     print("Invalid Choice.")