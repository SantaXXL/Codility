def solution(A):
    start_points = list()
    end_points = list()

    for center in range(len(A)):
        radius = A[center]
        start_points.append(center - radius)
        end_points.append(center + radius)

    start_points.sort()
    end_points.sort()
    start_points_counter = 0  # starting points of every disc
    end_points_counter = 0  # ending points of every disc
    result = 0  # how many interesctions we've encountered so far
    intersections = 0  # how many discs are intersecting at the given point

    while start_points_counter < len(A):
        # when a new disc appears, it will intersect with all "not-ended" discs
        if start_points[start_points_counter] <= end_points[end_points_counter]:
            result += intersections
            intersections += 1
            start_points_counter += 1
            continue

        # it means that we have encounted an ending of a disc
        if end_points[end_points_counter] <= start_points[start_points_counter]:
            intersections -= 1
            end_points_counter += 1

        if result > 1e7:
            return -1

    return result
