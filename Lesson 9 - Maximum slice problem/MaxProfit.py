def solution(A):
    if len(A) < 2:
        return 0

    max_global_diff = max_local_diff = 0
    current_min = A[0]

    for i in range(1, len(A)):
        max_local_diff = A[i] - current_min
        if current_min > A[i]:
            current_min = A[i]
        max_global_diff = max(max_global_diff, max_local_diff)

    return max_global_diff
