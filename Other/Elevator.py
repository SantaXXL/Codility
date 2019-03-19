def solution(A, B, M, X, Y):
    people_taken = 0  # people that left the queue
    floor_counter = 0  # visited floors, ground floor including

    while people_taken != len(A):
        weight = 0
        people_counter = 0
        temp = people_taken
        # calculate how many people elevator can take
        while people_taken != len(A) and weight + A[temp + people_counter] <= Y and people_counter + 1 <= X:
            people_counter += 1
            weight += A[people_taken]
            people_taken += 1

        pressed_buttons = set()
        for i in range(people_counter):  # unique floors
            pressed_buttons.add(B[temp + i])
        floor_counter += len(pressed_buttons) + 1
        # +1 == remember about ground floor
    return floor_counter


assert solution([40, 40, 100, 80, 20], [3, 3, 2, 2, 3], 3, 5, 200) == 6
assert solution([60, 80, 40], [2, 3, 5], 5, 2, 200) == 5
