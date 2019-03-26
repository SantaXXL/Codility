def solution(N):
    min_perimeter = 1e15
    i = 1
    while i * i <= N:
        if N % i == 0:
            perimeter = 2 * (i + N/i)
        i += 1
        if perimeter < min_perimeter:
            min_perimeter = perimeter

    return int(min_perimeter)
