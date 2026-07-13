# for loop
for i in range(19):
              print(i)

name = "Sajawal"
for number in name:
        print(number)

for i in range(1 , 100 , 2):
        print(i)

# while loop

count = 6
while count <= 12:
        print(count)
        count += 1


# mini projects


# multiplication of number 
number = int(input("Enter The Number = "))
for i in range(1,11):
        result = number * i
        print(f"{number} * {i} = {result}")


Number = int(input("Enter The Number = "))
i = 1
while i <= 10:
        result = Number * i
        print(f"{Number} * {i} = {result}")

        i = i + 1
      
# sum of numbers

sum = 0
for num in range(1 , 101):
        sum = sum + num
        print(sum)


sum = 0
num = 1
while num <= 100:
        sum = sum + num
        num += 1

        print(sum)

        

for i in range(1 , 101):
        print("Welcome")


# password checker

password = ""

while password != "Sajawal123":
        password = input("Enter Your Password = ")
print("Login Successfull")
        
