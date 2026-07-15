class Employee:

  def __init__(self , name , salary):
    self.name = name
    self.__salary = salary

  
  def get_salary(self):
    return self.__salary
  
  def set_salary(self , amount):
    if amount < 0:
      print("Salaary cannot be negative")
    else:
      self.__salary += amount

  def show_details(self):
    print("Name: " , self.name)
    print("Salary: " , self.__salary)


employee = Employee("Sajawal" , 0)

employee.show_details()

employee.set_salary(200000)

print(employee.get_salary())
