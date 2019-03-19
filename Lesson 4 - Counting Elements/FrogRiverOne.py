def solution(X, A):
    a = set()
    for i in range(len(A)):
        # sets can contain only unique values, hence adding
        # already present in set number doesn't change set's size
        a.add(A[i])
        if len(a) == X:
            return i
    return -1
