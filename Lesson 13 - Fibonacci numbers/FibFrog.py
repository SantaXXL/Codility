def generate_fib_numbers(n):
    fib_set = [1, 2]
    i = 2
    while True:
        fib_set.append(fib_set[i - 1] + fib_set[i - 2])
        if fib_set[i] >= n:
            fib_set.pop()
            return fib_set
        i += 1


def solution(A):
    if len(A) <= 2:
        return 1
    # add 0 at the beginning - just for convience, to skip writing A[i - 1]
    A.insert(0, 0)
    A.append(1)  # implies the final jump
    fib_set = generate_fib_numbers(len(A))

    # [-1], because we want to return -1 in case of no route
    jump_arr = [-1] * len(A)
    offset = 0
    # initialize the array - mark, when the first jump is possible
    for i in fib_set:
        if A[i] == 1:
            jump_arr[i] = 1

    # in case we can cross the river with 1 jump
    if jump_arr[-1] == 1:
        return 1

    # the idea is as follows:
    # - find the first unvisited leaf
    # - find all other leafs that you can reach from this leaf
    # - go to the next leaf and from here check all the other leafs that you can reach
    # - and so on

    for i in range(0, len(jump_arr)):
        if jump_arr[i] == -1:
            continue
        offset = i
        for j in fib_set:
            if j + offset >= len(A):
                break
            if A[j + offset] == 1:
                if jump_arr[j + offset] > jump_arr[i] + 1:
                    jump_arr[j + offset] = jump_arr[i] + 1
                elif jump_arr[j + offset] == -1:
                    jump_arr[j + offset] = jump_arr[i] + 1

    return jump_arr[-1]


solution([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0])
