import math


def solution(A):
    if len(A) < 3:
        return 0
    if len(A) == 3:
        return 1 if A[0] < A[1] > A[2] else 0

    # firstly, determine where are the peaks
    peak_counter = 0
    arr = list()

    for i in range(1, len(A) - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            arr.append(i)
            peak_counter += 1

    # the maximum possible amount of flags is
    # either floor(sqrt(len(A))) + 1 or number of peaks
    max_possible_flags = int(
        min(peak_counter, 1 + math.floor(math.sqrt(len(A)))))

    if max_possible_flags == 0:
        return 0

    upper = max_possible_flags
    lower = 0

    # the idea is as follows:
    # set starting point in the middle - max_possible_flags/2
    # then, if max_possible_flags/2 flags can be set, check if
    # (max_possible_flags+max_possible_flags/2)/2 = 3/4*max_possible_flags
    # can be set. And so on.
    while lower < upper:
        K = (upper + lower + 1) // 2
        counter = 1
        P = arr[0]
        for i in range(1, len(arr)):
            Q = arr[i]
            if abs(P - Q) >= K:
                if counter == K:
                    break
                counter += 1
                P = Q

        if counter == max_possible_flags:
            return max_possible_flags

        # if we can't set K flags, then we cannot set K+1, K+2,... flags as well
        if counter < K:
            upper = K - 1
            # flag indicates that we will have to substract 1 from the final result
            flag = True
        # if we can set K flags, then we can set K-1, K-2,... flags as well
        else:
            flag = False
            lower = K + 1

    if flag:
        return K - 1
    else:
        return K
