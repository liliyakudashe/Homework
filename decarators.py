def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if is_prime_num(result):
            print("Простое")
        else:
            print("Состовное")
        return result
    return wrapper


def is_prime_num(num):
    if num < 2:
        return False
    return True


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
