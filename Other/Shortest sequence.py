def solution(N):
    counter = 0
    while N != 0:
        print(N)
        if N % 2 == 0:
            N /= 2
        else:
            N -= 1
        counter += 1
    return counter
