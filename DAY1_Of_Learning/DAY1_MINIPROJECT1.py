# Student Management System

students = []

def add_student():
  name = input("Enter Student Name = ")
  students.append(name)
  print("Student Added Successfully")

def remove_student():
  name = input("Enter Student Name = ")
  students.remove(name)
  print("Student Removed")

def show_student():
  for student in students:
    print(student)



while True:

    print("\n***** Student Management System *****")

    print("1. Add Student")
    print("2. Remove Student")
    print("3. Show Students")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
      add_student()
    elif choice == "2":
      remove_student()
    elif choice == "3":
      show_student()
    elif choice == "4":
      print("Goodbye")
      break
    else:
      print("Invalid Choice")
