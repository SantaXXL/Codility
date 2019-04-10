def solution(A):
    N = len(A)
    count = dict()

    # count how many times each number is in A
    for i in A:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    divisors = dict()

    for i in count:
        divisors[i] = set()

    max_A = max(count)

    for i in divisors:
        if 2 * i > max_A:  # if max_A == 10, then the max divisior is 5
            continue
        divisor = 2 * i
        while divisor <= max_A:
            # if i == 2 and max_A == 10, then it will go like this:
            # check if 4 exists in count (which is, in fact, checking, if it exists in A)
            # notice, that we skip start from 2*i, since "i" will always be divisior of "i"
            # check if 2 is present among divisors of 4
            # if it is not, then add 2 to divisiors of 4
            # then check if 6 exists in count and if so, then if 2 is present among it's divisors
            # then do the same for 8
            # and for 10
            # and then change the value of "i"
            if divisor in count and i not in divisors[divisor]:
                divisors[divisor].add(i)
            divisor += i

    result = [0] * N

    for i in range(0, N):
        # if, for example, A = [1,1,1,2,2,2,3,3,3], then, for i == 7, for example (A[7] == 3)
        # firstly, substract the number of all "3"s
        result[i] = N - count[A[i]]
        for j in divisors[A[i]]:
            # the only divisor of 3 other than 3 is "1"
            # substract the number of all "1"s that exist in array A
            result[i] -= count[j]
    return result
