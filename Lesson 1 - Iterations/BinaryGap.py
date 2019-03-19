def solution(N):
    num = bin(N)
    max_gap = 0
    counter = 0

    for i in range(2, len(num)):
        if num[i] == '1':
            if counter > max_gap:
                max_gap = counter
            counter = 0
        elif num[i] == '0':
            # number converted to binary will always start with 1,
            # hence we will never encounter situation like '0000000101', that is
            # with a bunch of '0' with no '1' at the beginning
            counter += 1
    return max_gap
