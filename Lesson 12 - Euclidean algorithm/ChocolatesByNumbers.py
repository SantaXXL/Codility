def solution(N, M):
    # find gcd of N and M
    gcd = gcd_fun(N, M)

    # and then find lcm of N and M
    lcm = N * M / gcd

    return lcm/M


def gcd_fun(a, b):
    if a % b == 0:
        return b
    else:
        return gcd_fun(b, a % b)
