# 10 + 20 the 10 and 20 are operands and + is operator
# types of operator are 
# 1. Arithmetic Operators 
# 2. Comparison Operators
# 3. Logical Operators 
# 4. Assignment Operators 
# 5. Membership Operators 
# 6. Identity Operators 
# 7. Bitwise Operators 



#1. Arithmetic Operators  make calculations
# Addition
# price = 500
# delivery_fee = 100

# total = price + delivery_fee

# print(total)

# substraction
# balance = 10000
# withdraw = 2500

# remaining = balance - withdraw

# print(remaining)

# multiplication
# price = 250
# quantity = 4

# total = price * quantity

# print(total)

# division
# marks = 450
# subjects = 5

# average = marks / subjects

# print(average)

# floor division thorw the deciml part from the answer like 9.89 the answer will be 9 and symbol is //

# % this gives the remainder after division

# exponent ** means raise to the power means if 2**3 the answer will be 8

# WHOLE EXAMPLE

num1 = 50
num2 = 5

print(f"ADDITION = {num1 + num2}")
print(f"Subtraction = {num1 - num2}")
print(f"Multiplication = {num1 * num2}")
print(f"Division = {num1 / num2}")
print(f"Floor Division = {num1 // num2}")
print(f"Modulo = {num1 % num2}")
print(f"Exponent = {num1 ** num2}")




# 2.  Comparison Operators makes decisions


# == operator
username = "SAJAWAL"

print(username == "SAJAWAl")

# != operator

country = "Pakistan"
print(country != "India")


# > operator and < operator

age = 19
if age > 18:
             print("Adult")
else:
        print("Not Adult")

Age = 17
if Age < 18:
             print("Not Adult")
else:
        print("Adult")
      

# WHOLE EXAMPLE

age = 21

print(age == 21)
print(age != 18)
print(age > 18)
print(age < 30)
print(age >= 24)
print(age <= 25)

name = "Sajawal"
print(name == "Sajawal")
print(name != "Sajawal")