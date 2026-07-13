# Data Structure
# List
# Tuple
# Set
# Dictionary


# LISTS    lists are mutable
students = ["Sajawal" , "Jameel" , "Khan"]
print(students)


students[1] = "Jamil"

print(students)


students.append("Rajpoot")
print(students)

students.insert(2 , "Rana")

print(students)


for student in students:
  print(student)
  if "Rana" in student:
    print("Student Found")
    print(len(students))



# TUPLES

fruits = ("APPLE" , "BANANA" , "MANGO" , "ORANGE" , "GRAPES")
print(fruits[0])
print(fruits[4])

for fruit in fruits:
  print(fruit)


# unpacking a tuple
student = ("Sajawal" , 19 , "BSCS" , "Python_Backened")

name , age , degree , course = student

print(name)
print(age)
print(degree)
print(course)
