def multiply(*args):
    total = 1
    for numbers in args:
        total *= numbers
    return total


def even_or_odd(numbers):
    if numbers % 2 == 0:
        return (f'{numbers} NUMBER IS EVEN')
    return (f'{numbers} NUMBER IS ODD')


multiplication = multiply(1, 2, 3, 4, 5)
print(multiplication)

print(even_or_odd(1))
print(even_or_odd(2))
print(even_or_odd(3))
print(even_or_odd(4))
