def greet(name):
     print(f"Welcome {name}")

greet("Sajawal")
greet("Jameel")


# Introduction
def introduce(name , age):
     print(f"My name is {name}")
     print(f"My age is {age}")

introduce("Sajawal" , 20)

# basic calculations

def add(a , b):
     return a + b

def sub(a , b):
     return a - b

def mul(a , b):
     return a * b

def div(a , b):
     return a / b

print(add(5 , 4))
print(sub(3 , 9))
print(mul(9 , 3))
print(div(4 , 4))



# deep concpets about functions

# percentage calculator
def calculate_percentage(obtain_marks , total_marks):
     return obtain_marks / total_marks * 100
print(calculate_percentage(930 , 1100))

# grades checker
def check_grade(grades):
     if grades >= 90:
          return "A+"
     elif grades >= 80:
          return "A"
     elif grades >= 70:
          return "B"
     elif grades >= 60:
          return "C"
     else:
          return "F"
print(check_grade(30))
