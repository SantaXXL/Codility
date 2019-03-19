def solution(S):
    stack = list()
    if not S:
        return 1
    for i in S:
        if not stack and i == '(':
            stack.append(i)
            continue
        elif not stack and i == ')':
            return 0

        if i == '(':
            stack.append(i)
        else:
            stack.pop()

    if stack:
        return 0
    else:
        return 1
