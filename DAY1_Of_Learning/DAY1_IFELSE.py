# Even Odd checker

number = int(input("Enter Any Number = "))
if number % 2:
              print("Even Number")
else:
              print("Odd Number")

# Age Eligibilty Checker

age = int(input("Enter Your Age = "))
if age > 18:
        print("You Can Vote")
else:
        print("You Cannot Vote")


# Grades Checker

grades = int(input("Enter The Grades = "))

if grades >= 90:
        print("A+")
elif grades >= 80:
            print("A")
elif grades >= 70:
        print("B")
elif grades >= 50:
        print("C")
else:
        print("F")