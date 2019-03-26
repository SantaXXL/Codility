def solution(A):
    max_so_far = global_max = min_so_far = A[0]
    for i in range(1, len(A)):
        if A[i] == 0:
            max_so_far = min_so_far = 0
        else:
            temp = max_so_far
            max_so_far = max(max_so_far, max_so_far *
                             A[i], min_so_far * A[i], A[i])
            min_so_far = min(min_so_far, min_so_far * A[i], temp * A[i], A[i])

        global_max = max(global_max, max_so_far)

    return global_max
