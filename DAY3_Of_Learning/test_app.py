import pytest
from app import *


# Edge Case 1
def test_divide_by_zero():

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


# Edge Case 2
def test_negative_age():

    assert is_adult(-5) == False


# Edge Case 3
def test_exactly_18():

    assert is_adult(18) == True


# Edge Case 4
def test_empty_password():

    assert check_password("") == False


# Edge Case 5
def test_empty_list():

    assert largest([]) is None


# Edge Case 6
def test_all_duplicates():

    assert remove_duplicates([5,5,5,5]) == [5]


# Edge Case 7
def test_empty_username():

    assert login("") == False


# Edge Case 8
def test_over_withdraw():

    assert withdraw(1000,5000) == False


# Edge Case 9
def test_negative_factorial():

    with pytest.raises(ValueError):
        factorial(-2)


# Edge Case 10
def test_first_item_empty_list():

    with pytest.raises(IndexError):
        get_first([])


# Edge Case 11
def test_negative_square_root():

    with pytest.raises(ValueError):
        square_root(-16)