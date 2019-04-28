import time


# see https://www.nayuki.io/page/fast-fibonacci-algorithms

def calculate_fibonacci_1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return calculate_fibonacci_1(n - 1) + calculate_fibonacci_1(n - 2)


def calculate_fibonacci_2(n):
    fib = [0] * n
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n-1]


def calculate_fibonacci_3(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def calculate_fibonacci_4(n):
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec == '1':
            v1, v2, v3 = v1+v2, v1, v2
    return v2


def calculate_fibonacci_5(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = calculate_fibonacci_5(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


n = 30

start = time.time()
calculate_fibonacci_1(n)
end = time.time()
print(end - start)

start = time.time()
calculate_fibonacci_2(n)
end = time.time()
print(end - start)

start = time.time()
calculate_fibonacci_3(n)
end = time.time()
print(end - start)

start = time.time()
calculate_fibonacci_4(n)
end = time.time()
print(end - start)

start = time.time()
calculate_fibonacci_5(n)
end = time.time()
print(end - start)
