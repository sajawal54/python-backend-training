import json 
from pathlib import Path
student = [{
  "name": "Sajawal",
  "age" : 19
} , {
  "name" : "Jameel",
  "age" : 20
} , {
  "name" : "Rajpoot",
  "age" : 21
}]

# dump means add data to the file
file_path = Path(__file__).parent / "student.json"
with open(file_path , "w") as file:
  json.dump(student , file , indent=4)

# load means read data from the file
with open(file_path , "r") as file:
 content =  json.load(file)
 print(content)