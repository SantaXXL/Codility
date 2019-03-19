def solution(A):
    size = 0
    for i in A:
        if size == 0:
            size = 1
            value = i
        elif i == value:
            size += 1
        else:
            size -= 1

    counter = 0
    for i in A:
        if i == value:
            counter += 1

    if counter <= len(A) // 2:
        return - 1

    for i in range(len(A)):
        if A[i] == value:
            return i


# algorithm from codility's reading material
