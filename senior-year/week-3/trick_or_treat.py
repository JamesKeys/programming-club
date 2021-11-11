import math

def find_furthest(locations: list, curr_optimal: list):
	"""
	Finds the two furthest points from the current optimal point and returns.
	:param locations: 2d list containing all houses in [[x1,y1],[x2,y2],[x3,y3]...] format
	:param curr_optimal: list containing current optimal point in [x,y] format
	:returns: 2d list of furthest two houses in [[x1,y1],[x2,y2]] format
	"""
	distances = []
	for location_i in locations:
		distance_i = math.sqrt(abs(location_i[0]-curr_optimal[0])**2+location_i[1]**2)
		distances.append(distance_i)
	ret_val = [max(distances)]
	distances.remove(max(distances))
	ret_val.append(max(distances))
	return ret_val
def find_center_point(locations: list):
	"""
	Takes two points and returns the point on the x-axis which is either the
	minimum distance of one point with the other distance still being less, or
	the equidistant point.
	:param locations: 2d list containing two house coordinates in [[x1,y1],[x2,y2]] format
	:returns: list of new center point on x-axis in format [x,y]
	"""
	distances = []
	if locations[0][1] > math.sqrt(abs(locations[1][0]-locations[0][0])**2+))

while True:
	num_houses = int(input())
	if num_houses == 0:
		break
	if num_houses == 1:
		location = [float(x) for x in input().split()]
		print("{:.12f} {:.12f}".format(location[0], 0.0))
	else:
		locations = []
		for house_i in range(num_houses):
			locations.append([float(x) for x in input().split()])
		curr_optimal = [0,0]
		is_updating = True
		
		while is_updating:
			
			print(find_furthest(locations, curr_optimal))
			
		
	input()