def solution(N, A):
    arr = [0] * N
    max_val_curr = 0
    max_val_all = 0
    # The basic idea is as follows:
    # Track the maximum value and instead of performing operation "max counter"
    # every time, when N + 1 is detected, just do it once (second for loop).
    # In "increase(X)" case, just remember about the above and do a few extra
    # comparisons

    for i in A:
        if i >= 1 and i <= N:
            if arr[i - 1] <= max_val_all:
                arr[i - 1] = max_val_all + 1
                if max_val_curr < max_val_all + 1:
                    max_val_curr = max_val_all + 1
            else:
                arr[i - 1] += 1
                if arr[i - 1] > max_val_curr:
                    max_val_curr = arr[i - 1]

        elif i == N + 1:
            max_val_all = max_val_curr

    for i in range(len(arr)):
        if arr[i] < max_val_all:
            arr[i] = max_val_all

    return arr
