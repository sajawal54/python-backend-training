# word frequency counter
sentence = input("Enter Your sentence = ")

words = sentence.split()

frequency = {}

for word in words:
    
    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1
    

for word , count in frequency.items():
    print(word , ":" , count)



# duplicate remover

numbers = [1, 3 , 2 , 3 ,2, 5 , 6,4 , 9,7, 8]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)

# testing
names = [
    "Ali",
    "Ahmed",
    "Ali",
    "Sajawal",
    "Ahmed"
]

unique_names = []

for name in names:
    if name not in unique_names:
        unique_names.append(name)

print(unique_names)

# logging errors to files
from pathlib import Path
file_path = Path(__file__).parent / "error.log"

user_input = input("Enter Your age = ")
try:
    number = int(user_input)
    print(number)

except ValueError:
    with open(file_path , "a") as file:
        file.write(f"Invalid Input:  {user_input}")

    print("Error Saved")

