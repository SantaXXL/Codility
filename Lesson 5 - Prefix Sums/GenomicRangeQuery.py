def solution(S, P, Q):

    # not the most elegant solution, but it works just fine

    A = (len(S) + 1) * [0]
    C = (len(S) + 1) * [0]
    G = (len(S) + 1) * [0]
    for i in range(len(S)):
        a = c = g = 0
        if S[i] == 'A':
            a = 1
        elif S[i] == 'C':
            c = 1
        elif S[i] == 'G':
            g = 1
        A[i + 1] = A[i] + a
        C[i + 1] = C[i] + c
        G[i + 1] = G[i] + g

    arr = list()
    for i in range(len(P)):
        if P[i] == Q[i]:
            if S[P[i]] == 'A':
                arr.append(1)
            elif S[P[i]] == 'C':
                arr.append(2)
            elif S[P[i]] == 'G':
                arr.append(3)
            else:
                arr.append(4)
        else:
            if A[Q[i] + 1] - A[P[i]] > 0:
                arr.append(1)
            elif C[Q[i] + 1] - C[P[i]] > 0:
                arr.append(2)
            elif G[Q[i] + 1] - G[P[i]] > 0:
                arr.append(3)
            else:
                arr.append(4)

    return arr
