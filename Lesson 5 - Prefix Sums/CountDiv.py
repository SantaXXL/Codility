import math


def solution(A, B, K):
    entry_point = math.ceil(A / K) * K
    exit_point = math.floor(B / K) * K

    return int((exit_point - entry_point) / K + 1)
