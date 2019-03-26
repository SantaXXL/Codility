# the idea is simple
# firstly, create a list that stores positions of peaks
# secondly, find a divisor of len(A), starting from the seconed biggest one,
# that is, for 36 it would be 18 (we need to find at least 2 blocks; block size
# must be at least 3)
# and then check if there is at least one peak in every block
# if so, then "counter == i" condition is true


def solution(A):
    N = len(A)
    if N < 3:
        return 0

    arr = list()
    for i in range(1, N - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            arr.append(i)

    for i in range(N, 0, -1):
        if N % i == 0:
            K = N / i
            if K < 3:  # block size must be at least 3
                continue
            counter = 0
            for a in arr:
                if a >= counter * K and a < (counter + 1) * K:
                    counter += 1
            if counter == i:
                return counter
    return 0
