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
