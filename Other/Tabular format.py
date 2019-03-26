def solution(N, K, A):
    max_value = max(A)
    cell_width = len(str(max_value))
    top_edge = ('+' + '-' * cell_width) * N + '+'
    bottom_edge = top_edge

    for i in range(0, len(A), N):
        row = ''
        print(top_edge)
        for n in range(N):
            row += '|' + \
                (cell_width - len(str(A[i + n]))) * ' ' + str(A[i + n])
        row += '|'
        print(row)
    print(bottom_edge)
