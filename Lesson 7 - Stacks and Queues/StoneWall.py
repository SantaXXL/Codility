def solution(H):
    stack = list()
    block_counter = 0
    for h in H:
        if stack:
            while stack and h < stack[-1]:
                stack.pop()
        if not stack:
            stack.append(h)
            block_counter += 1
        else:
            if h > stack[-1]:
                stack.append(h)
                block_counter += 1

    return block_counter

# stack is empty, append the number
# if next number in array is bigger than the last in stack, append it
# if next number in array is smaller than the last in stack, remove
# elements from stack that are bigger than this number, for instance:
# stack = [5,7,9], h = 6
# pop 9, pop 7, append 6 => stack = [5,6]
