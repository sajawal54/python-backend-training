def divide(a, b):
    return a / b


def is_adult(age):
    return age >= 18


def check_password(password):
    return len(password) >= 8


def largest(numbers):
    if len(numbers) == 0:
        return None
    return max(numbers)


def remove_duplicates(numbers):
    return list(set(numbers))


def login(username):
    return username != ""


def withdraw(balance, amount):
    if amount > balance:
        return False
    return True


def factorial(number):
    if number < 0:
        raise ValueError("Negative number")
    if number == 0:
        return 1

    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def get_first(items):
    return items[0]


def square_root(number):
    if number < 0:
        raise ValueError("Negative number")
    return number ** 0.5