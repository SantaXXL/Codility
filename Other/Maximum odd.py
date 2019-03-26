def solution(A, N):
    max_value = -10001
    for i in A:
        if i % 2 != 0 and i > max_value:
            max_value = i
    return max_value
