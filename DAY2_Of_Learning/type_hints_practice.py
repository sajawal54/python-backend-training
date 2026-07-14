# type hints kisi bhi developer ko ye smajhne me madad kerte hain ke function ke jo paramters hain ya jo vlaues hain unki datatypes kiya hain
def add(a:int , b:int) -> int:
  return a + b

def multiply(a : float , b : float) -> float:
  return a * b

def greet(name : str) -> str:
  return name

def is_adult(age : int) -> bool:
  return True