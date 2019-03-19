def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def solution(A):
    for i in range(len(A)):
        while 0 < A[i] \
                and A[i] - 1 < len(A) \
                and A[i] != i + 1 \
                and A[i] != A[A[i] - 1]:
            swap(A, i, A[i] - 1)
    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1
    return len(A) + 1

# example of how the algorithm works
# input data: solution([1, 6, 6, 2, 4, 1, 2, 3])
# and then (after every swap)
# [1, 6, 6, 2, 4, 1, 2, 3]
# [1, 1, 6, 2, 4, 6, 2, 3]
# [1, 2, 6, 1, 4, 6, 2, 3]
# [1, 2, 6, 4, 1, 6, 2, 3]
# [1, 2, 3, 4, 1, 6, 2, 6]
#
# in other words, put first occurence of every valid number
# where valid means: x > 0, x < len(A) - 1
# in the right position of the array.
# This way we can skip sorting negative numbers, numbers greater than len(A),
# and repeats
