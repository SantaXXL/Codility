def solution(A):
    if len(A) < 3:
        return 0
    A.sort()
    if A[- 1] < 1:
        return 0

    for i in range(len(A)):
        if A[i] > 0:
            index_of_first_positive = i
            break

    for i in range(index_of_first_positive, len(A) - 2):
        # note, that since A[i + 2] - in sorted array - is bigger
        # than A[i] and A[i + 1], we do not need to check the other
        # two conditions, since they are automatically fulfilled
        if A[i] + A[i + 1] > A[i + 2]:
            return 1
    return 0
