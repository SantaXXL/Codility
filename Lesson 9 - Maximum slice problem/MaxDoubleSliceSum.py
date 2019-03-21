def solution(A):
    if len(A) < 4:
        return 0
    max_sum_end = len(A) * [0]
    max_sum_start = len(A) * [0]

    for i in range(1, len(A) - 1):
        max_sum_end[i] = max(0, max_sum_end[i - 1] + A[i])
    for i in range(len(A) - 2, 1, -1):
        max_sum_start[i] = max(0, max_sum_start[i + 1] + A[i])

    max_value = 0
    for i in range(1, len(A) - 1):
        max_value = max(max_value, max_sum_end[i - 1] + max_sum_start[i + 1])

    return max_value
