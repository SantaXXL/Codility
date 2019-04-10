def sieve(N):
    # firstly, perform a standard sieve of Eratosthenes
    # note that if, for example, N = 50, then we need to
    # search for primes no bigger than 25
    # this is because the smallest prime is 2, hence we will
    # multiply 25 times
    sieve = [True] * (N//2) + 1
    sieve[0] = sieve[1] = False
    i = 2
    while (i * i <= N//2):
        if (sieve[i]):
            k = i * i
            while (k <= N//2):
                sieve[k] = False
                k += i
        i += 1

    # find semiprimes
    semiprimes = [0] * (N + 1)
    for i in range(0, len(sieve)):
        if not sieve[i]:
            continue
        temp = i
        counter = 0
        while i * temp <= N:
            counter += 1
            semiprimes[i * temp] = i * temp
            while i + counter < len(sieve) and sieve[i + counter] == False:
                counter += 1
            temp = i + counter

    # transform semiprimes into prefix sums
    counter = 0
    for i in range(3, len(semiprimes)):
        if semiprimes[i] != 0:
            counter += 1
            semiprimes[i] = counter
        else:
            semiprimes[i] = counter
    return semiprimes


def solution(N, P, Q):
    if N == 1:
        return [0]

    prefix_sum = sieve(N)
    result = [0] * len(P)

    for i in range(len(P)):
        result[i] = prefix_sum[Q[i]] - prefix_sum[P[i] - 1]

    return result
