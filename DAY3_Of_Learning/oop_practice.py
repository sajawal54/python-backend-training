# class organize python programming structure and functions inside a class are called methods
class Car:
  
      def __init__(self , brand , color):
            self.brand = brand
            self.color = color

car1 = Car("TOYOTA" , "WHITE")
car2 = Car("HONDA" , "PURPLE")

print(car1.brand)
print(car1.color)

print(car2.brand)
print(car2.color)


# adding a function into class
class Car:
      
     def __init__(self , brand , color):
            self.brand = brand
            self.color = color

     def show_info(self):
           print("Brand: " , self.brand)
           print("Color: " , self.color)

car1 = Car("TOYOTA" , "BLACK")
car1.show_info()

# A student record example
class Student:
      
      def __init__(self , name , age , marks):
            self.name = name
            self.age = age
            self.marks = marks

      def show_details(self):
            print("Name: " , self.name)
            print("Age: " , self.age)
            print("Marks: " , self.marks)

student1 = Student("Sajawal" , 19 , 45)
student2 = Student("Khan" , 19 , 34)

student1.show_details()
student2.show_details()
        
            