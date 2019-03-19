def solution(A):
    arr = [False] * len(A)  # sets would fit for this solution as well
    for i in A:
        if i > len(A):
            return 0
        if arr[i - 1] == True:
            return 0
        arr[i - 1] = True
    if False in arr:
        return 0
    else:
        return 1
