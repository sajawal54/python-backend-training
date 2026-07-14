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



# SETS represented by {} and automatically remove duplicate value

students = {"Sajawal" , "Jameel" , "Rajpoot" , "Sajawal" , "Jameel"}
print(students)


students.add("Khan")
print(students)

students.remove("Khan")
print(students)

# union in sets

present_students = {"Sajawal" , "Rajpoot" , "Jameel"}
absent_students = {"Ali", "Rajpoot", "Aqib"}

print(present_students | absent_students)

# intersection in sets

print(present_students & absent_students)

# difference in sets
print(present_students - absent_students)

students = {"ALI" , "Ahmad" , "Mehar"}
for student in students:
  print(student)



numbers = [1, 2, 3, 2, 4, 5, 1, 6, 5]

unique_numbers = set(numbers)

print(unique_numbers)





python_students = {"Ali", "Ahmed", "Usman"}

django_students = {"Ahmed", "Usman", "Sajawal"}

print(python_students | django_students)
print(python_students & django_students)
print(python_students - django_students)
print(django_students - python_students)



# DICTIONARY  allow us to store data as key value pair ;like objects in databases

form = {
  "name": "Sajawal",
  "age": 21,
  "city": "Manga Mandi Lahore"
}

print(form["name"])
# to get none if result dont match insteadof error
print(form.get("email"))

# adding new data
form["email"] = "abc@gmail.com"

print(form)



for key in form:
  print(key)

  for value in form.values():
    print(value)


    student = {
    "name": "Sajawal",
    "age": 21,
    "course": "Python Backend",
    "city": "Lahore"
}

for key, value in student.items():
    print(f"{key}: {value}")