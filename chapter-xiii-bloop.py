# BlooP allows only bounded loops (for loop with predetermined set of values)

def two_to_the_three_to_the(n):
    three_pow = 1

    for i in range(n):
        three_pow = three_pow * 3

    two_pow = 1

    for i in range(three_pow):
        two_pow = two_pow * 2

    print(two_pow)

def is_prime(n):
    if n == 0:
        return False

    factor = 2

    for factor in range(2, n):
        if n % factor == 0:
            return False

    return True

def is_goldbach(n):
    for factor in range(2, n):
        if is_prime(factor) and is_prime(n - factor):
            return True
        factor = factor + 1

    return False

def factorial(n):
    output = 1

    for i in range(1, n + 1):
        output = output * i

    return output

def fibonacci(n):
    if n <= 2:
        return 1

    a = 1
    b = 1

    for i in range(2, n):
        new_a = b
        b = a + b
        a = new_a

    return b

