def solution(N):
    if not N:
        return 1
    stack = list()

    for i in N:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            if not stack:
                return 0
            if (i == ')' and stack[-1] == '(') or \
                (i == '}' and stack[-1] == '{') or \
                    (i == ']' and stack[-1] == '['):
                stack.pop()
            else:
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0
