# Задача 1
def math_func(operation):
    if operation == "add":
        return lambda x, y: x + y
    elif operation == "subtract":
        return lambda x, y: x - y
    elif operation == "multiply":
        return lambda x, y: x * y
    elif operation == "divide":
        return lambda x, y: x / y


add_func = math_func("add")
subtract_func = math_func("subtract")
multiply_func = math_func("multiply")
divide_func = math_func("divide")

print(add_func(2, 3))
print(subtract_func(5, 3))
print(multiply_func(2, 4))
print(divide_func(10, 2))

# Задача 2
square_lambda = lambda x: x ** 2


def square_def(x):
    return x ** 2


print(square_lambda(3))
print(square_def(3))


# Задача 3
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


rect = Rect(3, 4)
print(rect())
