def solution(A):
    # we have a few cases:
    # - only negative numbers
    # - only positive numbers
    # - non-negative / non-positive
    # - mixed of all the above
    # notice, that if we have for example
    # -5 -4 -3 -2 -1 0 1
    # then the maximum is (-5) * (-4) * 1
    # but for -5 -4 -3 -2 -1 0
    # the maximum is (-3) * (-2) * (-1)
    # ... and it turns out that for every case it will be either
    # a multiplicaiton of 3 last elements
    # or multiplication of two first and last one

    A.sort()
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])
