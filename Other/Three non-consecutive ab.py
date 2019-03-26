def solution(A, B):
    result = ''
    arr = [[0 for x in range(2)] for y in range(2)]

    if A > B:
        arr[0][0] = A
        arr[0][1] = 'a'
        arr[1][0] = B
        arr[1][1] = 'b'
    else:
        arr[0][0] = B
        arr[0][1] = 'b'
        arr[1][0] = A
        arr[1][1] = 'a'

    # crate 'aabaabaab...' or 'bbabbabba...' string to
    # level the amount of 'a's and 'b's left
    while arr[0][0] > arr[1][0] > 0:
        result += arr[0][1]
        result += arr[0][1]
        result += arr[1][1]
        arr[0][0] -= 2
        arr[1][0] -= 1

    # append 'ab' or 'ba' string multiple times, until the less
    # frequent character's counter will reach 0
    while arr[1][0] > 0:
        result += arr[0][1]
        result += arr[1][1]
        arr[0][0] -= 1
        arr[1][0] -= 1

    # and append, if there is any left, more frequent character
    while arr[0][0] > 0:
        result += arr[0][1]
        arr[0][0] -= 1

    return result
