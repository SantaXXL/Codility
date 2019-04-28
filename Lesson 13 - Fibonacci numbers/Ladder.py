def solution(A, B):
    if len(A) == 1:
        return [1]
    max_num = max(A)
    fib = [0] * max_num
    fib[0] = 1
    fib[1] = 2

    for i in range(2, max_num):
        fib[i] = fib[i - 1] + fib[i - 2]

    result = [0] * len(A)
    for i in range(0, len(A)):
        result[i] = fib[A[i] - 1] & (2 ** B[i] - 1)
    return result
