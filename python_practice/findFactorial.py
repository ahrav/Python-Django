def factorial(number):
    if number < 3:
        return number
    else:
        return number * factorial(number-1)

print(factorial(0))