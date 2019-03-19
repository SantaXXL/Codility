def solution(A):
    # firstly, our left side is just the first element of an array
    # and the right side is sum of the rest

    left = A[0]
    right = sum(A) - A[0]
    min_diff = abs(left - right)

    # and then move right, element after element, until the situation
    # is reversed
    for i in range(1, len(A) - 1):
        left += A[i]
        right -= A[i]
        if abs(left - right) < min_diff:
            min_diff = abs(left - right)
    return min_diff
