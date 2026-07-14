# for i in range(1 , 11):
#   print(i)

# students = ["Ali", "Sajawal" , "Rajpoot"]
# students.remove("Rajpoot")
# print(students)


# student = {
#   "name": "Sajawal",
#   "age":  21,
#   "email": "abc@gmail.com"
# }

# print(student["email"])

# for key , value in student.items():
#   print(f"{key} : {value}")



# students = [{"name" : "Sajawal" , "age" : 19 , "work" : "Python Backened"},
#               {"name" : "Jameel" , "age" : 19 , "work" : "Python Backened"},
#               {"name" : "RSJ" , "age" : 19 , "work" : "Python Backened"}
#               ]
  
# print(students[0])

# print(students[0]["work"])


# 1
# numbers  = [5 , 3 ,2, 3, 6, 5, 7, 2]

# unique_number = []

# for number in numbers:

#   if number not in unique_number:
      
#       unique_number.append(number)

# print(unique_number)

# # 2
# text = "Python Backened"
# count = 0

# vowels = "aeiouAEIOU"

# for letter in text:
#    if letter in vowels:
#       count += 1

# print(count)

# 3
# text = "Backened"

# reverse = " "

# for letter in text:
#    reverse = letter + reverse
# print(reverse)


# 4

# sentence = "python , django , python , flask , django , python"

# words = sentence.split()

# frequency = {}

# for word in words:
#    if word in frequency:
#       frequency[word] += 1

#    else:
#       frequency[word] = 1

# for word , count in frequency.items():
       
#       print(word , ":" , count)

# # 5

# numbers = [1,2,3,3,4,3,5,4,6,7,5]

# real = []

# for number in numbers:
#     if number not in real:
#         real.append(number)

# for number in real:
#     print(number)


# 1
# numbers = [89 , 45 , 54 , 98 , 90]
# largest = numbers[0]

# for number in numbers:
#   if number > largest:
#     largest = number
    
# print(largest)
  
# 2
# students = [
#   {"name" : "Sajawal" , "marks" : 90},
#   {"name" : "Jameel" , "marks" : 94},
#   {"name" : "Ali" , "marks" : 70},
#   {"name" : "Ahmad" , "marks" : 80}
# ]

# a = 0
# b = 0
# c = 0
# f = 0

# for student in students:
#   if student["marks"] >= 90:
#     a += 1
#   elif student["marks"] >= 80:
#     b += 1
#   elif student["marks"] >= 70:
#     c += 1
#   else:
#     f += 1


# print("A grade students are = " , a)
# print("B grade students are = " , b)
# print("C grade students are = " , c)
# print("F grade students are = " , f)


# import string
# def passwordchecker(password):

#   if len(password) < 8:
#     return "Password must be at least 8 characters"

#   if not any(char.islower() for char in password):
#     return "Password must containe at least one lower case"
  
#   if not any(char.isupper() for char in password):
#     return "Password must containe at least one upper case"
  
#   if not any(char.isdigit() for char in password):
#     return "Password must containe at least one digit"
  
#   special_character = string.punctuation 
#   if not any(char in special_character for char in password):
#     return "password must contain at least one special character"
  
#   return "Valid password"


# while True:
#  user_password =  input("Enter Your Password")
#  result = passwordchecker(user_password)
#  print(result)
# size = 5
# for i in range(size):
#       for j in range(size):
#          print("*" , end=" ")
#       print()

# rows = 5

# for i in range(1 , rows + 1):
#      for j in range(i):
#           print("*" , end=" ")
#      print()




