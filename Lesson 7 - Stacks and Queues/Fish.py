import math


def solution(A, B):
    global stack
    global size
    stack = [0] * len(A)
    size = 0
    for i in range(len(A)):
        if size == 0:
            push(-A[i]) if B[i] == 1 else push(A[i])
        elif B[i] == 1:
            push(-A[i])
        elif B[i] == 0:
            while size > 0 and stack[size - 1] < 0 and -stack[size - 1] < A[i]:
                pop()
            if size > 0 and stack[size - 1] > 0:
                push(A[i])
            elif size == 0:
                push(A[i])

    return size


def push(x):
    global size
    stack[size] = x
    size += 1


def pop():
    global size
    size -= 1
