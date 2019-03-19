def solution(A):
    min_average = 666666
    min_index = 0
    # Note, that the minimal average slice can be made of only 2 or 3 elements.
    # Consider such array: 100, 2, 3, 2, 3, 100
    # Clearly, the minimal avg slice is 2-3-2
    # But if we changed 3 to 2, or added another 2: 100, 2, 3, 2, 2, 3, 100
    # then the minimal avg slice is 2-2

    for i in range(len(A) - 2):
        average_2_elements = (A[i] + A[i + 1]) / 2
        average_3_elements = (A[i] + A[i + 1] + A[i + 2]) / 3
        if min_average > average_2_elements:
            min_average = average_2_elements
            min_index = i
        if min_average > average_3_elements:
            min_average = average_3_elements
            min_index = i
    if min_average > (A[-2] + A[-1]) / 2:
        min_index = len(A) - 2
    return min_index
