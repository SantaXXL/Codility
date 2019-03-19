def solution(A):
    arr = [0] * len(A)
    for i in range(1, len(A)):
        arr[i] = arr[i - 1] + A[i]
    total_sum = 0

    for i in range(0, len(A)):
        if A[i] == 0:
            total_sum += arr[-1] - arr[i]
            if total_sum > 1000000000:
                return -1
    return total_sum
