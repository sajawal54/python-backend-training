def addition():
  try:
      number_1 = int(input("Enter First Number = "))
      number_2 = int(input("Enter Second Number = "))

      return number_1 + number_2

  except ValueError:
     print("Value Should Be a Number")
   

def subtraction():
  try:
      number_1 = int(input("Enter First Number = "))
      number_2 = int(input("Enter Second Number = "))

      return number_1 - number_2

  except ValueError:
     print("Value Should Be a Number")


def division():
  try:
      number_1 = int(input("Enter First Number = "))
      number_2 = int(input("Enter Second Number = "))

      return number_1 / number_2

  except ValueError:
    print("Please enter numbers only.")
  except ZeroDivisionError:
     print("Divsion cannot be done with zero")


def show_menu():
  print("*********Student Calculator*********")
  print("1 for Addition")
  print("2 for Subtraction")
  print("3 for Division")
  print("4 for Exit")



while True:
 show_menu()
 choice = input("Enter Your Choice = ")

 if choice == "1":
   addition()
 elif choice == "2":
   subtraction()
 elif choice == "3":
    division()
 elif choice == "4":
  print("Thank you for using my calculator")
  break
 else:
  print("Invalid Choice")


