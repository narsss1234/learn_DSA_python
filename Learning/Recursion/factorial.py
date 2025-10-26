def factorial_of_a_number(value):
    if value == 1:
        return 1
    return value * factorial_of_a_number(value-1)

print(factorial_of_a_number(5))