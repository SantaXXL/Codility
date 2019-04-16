def solution(A, B):
    result = 0
    for a, b in zip(A, B):
        # firstly, find a greatest common divisor of A[i] and B[i]
        gcd_AB = find_gcd(a, b)
        # now, we need to notice, that every number is made of only prime numbers
        # for instance, 24 = 2 * 2 * 2 * 3
        # and the only other number, that has same prime divisors
        # can only be like this: 2^n * 3^n, n >= 1
        # so lets say we have 24 and 6
        # the gcd(6,24) is 6
        # then we check, what's the gcd(6,6) - it is 1
        # this tells us that there is no more primes that are both in A[i] and B[i]
        # then we divide 6 by gcd(24,6), which gives us 1. This means, that
        # 6 is only made of primes that are also divisor of 24.
        # Same thing goes for 24:
        # divide by 6 -> we got 4
        # find gcd(6,4) -> we got 2
        # divide 4 by 2 -> we got 2
        # find gcd(6,2) -> we got 2
        # divide 2 by 2 -> we got 1
        # and this means that 24 has also the same prime divisor that gcd(6,24) has
        if not does_consist_all_prime_divisors(a, gcd_AB):
            continue
        if not does_consist_all_prime_divisors(b, gcd_AB):
            continue
        result += 1

    return result


def does_consist_all_prime_divisors(num, gcd_AB):
    while num > 1:
        gcd = find_gcd(num, gcd_AB)
        if int(gcd) == 1:
            return False
        num /= gcd
    return True


def find_gcd(a, b):
    if a % b == 0:
        return b
    return find_gcd(b, a % b)
