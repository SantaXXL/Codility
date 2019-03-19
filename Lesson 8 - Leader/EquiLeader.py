def solution(A):
    size = 0
    for i in A:
        if size == 0:
            candidate = i
            size += 1
        elif candidate == i:
            size += 1
        else:
            size -= 1

    if size == 0:
        return 0

    occurances_of_leader = 0

    for i in A:
        if i == candidate:
            occurances_of_leader += 1

    if occurances_of_leader < len(A) // 2:
        return 0

    leader = candidate
    pairs_counter = 0
    leader_counter = 0

    for i in range(len(A)):
        if A[i] == leader:
            leader_counter += 1
        if leader_counter * 2 > i + 1 and \
                2 * (occurances_of_leader - leader_counter) > len(A) - (i + 1):
            pairs_counter += 1

    return pairs_counter

# notice, that there can be only one leader in the array
# first half of the program is like Dominator.py, while the other half
# checks how many pairs of equi leader exists
