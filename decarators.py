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

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        count = 0
        for i in range(1, result+1):
            if result % i == 0:
                count += 1
        return f"Простое {result}" if count == 2 else f"Составное {result}"
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
