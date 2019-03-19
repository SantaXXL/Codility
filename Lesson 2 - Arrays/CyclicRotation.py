def solution(A, K):
    if not A:
        return A
    K = K % len(A)
    # no rotation at all
    if K == 0:
        return A
    # add K last elements to the beginning of the array
    # and then remove K last elements from the array
    # note: this will create a copy of A, hence the less memory-consuming solution
    # would be to use deque from collections
    A = A[len(A) - K:] + A[:len(A) - K]
    return A
