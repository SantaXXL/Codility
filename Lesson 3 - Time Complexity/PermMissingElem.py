def solution(A):
    result = 0
    for i in range(len(A)):
        result += A[i] - (i + 1)
    return len(A) + 1 - result
