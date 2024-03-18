def multiply(multiplication):
    def operation(number):
        return number * multiplication
    return operation


operator = multiply(3)

print(operator(3))
