class Person:
  def __init__(self , name , age):
    self.name = name
    self.age = age


  def show_details(self):
    print("Name: " , self.name)
    print("Age: " , self.age)


class Student(Person):
  def __init__(self, name, age, roll_no):
    super().__init__(name, age)
    self.roll_no = roll_no

  def show_students(self):
    self.show_details()
    print("Roll No: " , self.roll_no)


student = Student("Sajawal" , 19 , 103)

student.show_students()


# method overriding means both the chiod and parent habe samw metheds but python overrides the patent method

class Animal:
  def Sound(self):
    print("Animal Have different sounds")

class Dog(Animal):
  def Sound(self):
    print("Dog sound is wowowowow")

dog = Dog()

dog.Sound()


# Compoition 
class Engine:

  def start(self):
    print("Engine started")


class Car:

  def __init__(self):
      self.engine = Engine()

  def start_car(self):
          
          self.engine.start()

  print("Car Starts")

car = Car()

car.start_car()

# another example

class Weapon:
   def attack(self):
      print("Boom")


class Player:
   def __init__(self):
       self.weapon = Weapon()

   def start_weapon(self):
      self.weapon.attack()

player = Player()

player.start_weapon()
