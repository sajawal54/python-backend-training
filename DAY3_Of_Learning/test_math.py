from math_operations import addition , subtract , divide
import pytest

def test_divide_by_zero():
  with pytest.raises(ZeroDivisionError):
    divide(10 , 0)

def test_add():
  assert addition(5 , 5) == 10


def test_subtrat(library):
  assert subtract(10 , 5) == 5

# so fixture is something if we are writing a single line or exporting or impoorting something like library so we dont have need to write the library in every code instead we will ponly choose this path as below and after we can use library as parameter
  @pytest.fixture
  def library():
      return library()