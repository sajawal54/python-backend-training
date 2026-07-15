

class Person:
 """
   Represent A person in the library
 """
 def __init__(self , name , age):
        self.name = name 
        self.age = age


 def show_details(self):
     print(f"Name: {self.name}")
     print(f"Age: {self.age}")


