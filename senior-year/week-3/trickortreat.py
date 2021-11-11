import math


def find_optimal(locations: list):
    """
	calculate the point on the y-axis which is equidistant between every combination
	of two points, and return the maximum of all distances.
	"""
    # this will hold the possible x values
    opt_points = []
    # this will hold the i'th distance for the i'th x value
    distances = []

    # for each location, excluding the last,
    for i in range(len(locations) - 1):
        # for each location not previously looked at,
        for i2 in range(i + 1, len(locations)):
            # if the locations have the same x-value,
            if locations[i2][0] - locations[i][0] == 0:
                # assign the x-value as the optimal
                A = locations[i][0]
                # assign the distance as the greater of the two y-values
                distances.append(max(abs(locations[i][1]), abs(locations[i2][1])))
            else:
                # math to find the equidistant point on y-axis
                A = ((locations[i2][1] ** 2 - locations[i][1] ** 2 - locations[i][0] ** 2 + locations[i2][
                    0] ** 2) / 2) / (locations[i2][0] - locations[i][0])
                # distance for each point to get to that point A
                dist_A = math.sqrt((locations[i][0] - A) ** 2 + locations[i][1] ** 2)
                # distance for i2 to get to (i1[0], 0) in case that's shorter
                dist_A1 = math.sqrt((locations[i2][0] - locations[i][0]) ** 2 + locations[i2][1] ** 2)
                # distance for i to get to (i2[0], 0) in case that's shorter
                dist_A2 = math.sqrt((locations[i][0] - locations[i2][0]) ** 2 + locations[i][1] ** 2)

                # if the minimum distance is i's x value, use that
                if min(dist_A, dist_A1, dist_A2) == dist_A1:
                    A = locations[i][0]
                    distances.append(abs(locations[i][1]))
                # if the minimum distance is i2's x value, use that
                elif min(dist_A, dist_A1, dist_A2) == dist_A2:
                    A = locations[i2][0]
                    distances.append(abs(locations[i2][1]))
                # otherwise, stick to what we have with A and the equidistant values
                else:
                    distances.append(math.sqrt((locations[i][0] - A) ** 2 + locations[i][1] ** 2))
            opt_points.append(A)

    # return the optimal worst-case scenario to give the minimum distance for all kids
    return opt_points[distances.index(max(distances))], max(distances)


while True:
    numHouses = int(input())
    if numHouses == 0:
        # end of tests
        break

    # get first house
    loc_0 = [float(x) for x in input().split()]

    if numHouses == 1:
        # print location of first house if that is the only one
        print_val = loc_0
    else:
        # locations will hold the extremes which are all we care about
        locations = [loc_0 for x in range(4)]

        # initialize extremes with location 0
        max_x, min_x, max_y, min_y = loc_0[0], loc_0[0], loc_0[1], loc_0[1]

        for house_i in range(1, numHouses):
            loc_i = [float(x) for x in input().split()]

            # assign to extreme if greater/less, then update value
            if loc_i[0] > max_x:
                locations[0] = loc_i
                max_x = loc_i[0]
            if loc_i[0] < min_x:
                locations[1] = loc_i
                min_x = loc_i[0]
            if loc_i[1] > max_y:
                locations[2] = loc_i
                max_y = loc_i[1]
            if loc_i[1] < min_y:
                locations[3] = loc_i
                min_y = loc_i[1]

        # find optimal value, with location(x) and distance being returned
        print_val = find_optimal(locations)

    # print
    print("{:.12f} {:.12f}".format(print_val[0], print_val[1]))
    input()