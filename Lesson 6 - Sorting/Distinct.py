def solution(A):
    a = set()
    for i in A:
        a.add(i)
    return len(a)


# version with sorting
def solution(A):
    if not A:
        return 0
    A.sort()
    counter = 1
    previous_num = A[0]
    for i in range(len(A)):
        next_num = A[i]
        if next_num != previous_num:
            counter += 1
            previous_num = next_num
    return counter
