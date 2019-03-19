def solution(A):
    x = 0
    for i in A:
        x ^= i
    return x

# 5 XOR 7, for example, is equal to 101 XOR 111 = 010 (binary) = 2 (decimal)
# 7 XOR 7, from the other side, is eqaul to 111 XOR 111 = 0
# in other words, XOR-ing a pair of identical numbers will produce '0'
# and 0 XOR anything = anything
