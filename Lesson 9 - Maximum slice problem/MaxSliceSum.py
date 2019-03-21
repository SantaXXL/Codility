def solution(A):
    max_global_slice = max_local_slice = A[0]

    for i in range(1, len(A)):
        max_local_slice = max(A[i], max_local_slice + A[i])
        max_global_slice = max(max_global_slice, max_local_slice)

    return max_global_slice
