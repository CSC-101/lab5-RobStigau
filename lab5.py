import data
import math
# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1 : data.Time, time2 : data.Time) -> data.Time:
    seconds = time1.second + time2.second
    minutes = 0
    hours = 0
    if seconds > 60:
        seconds -= 60
        minutes += 1
    minutes += (time1.minute + time2.minute)
    if minutes > 60:
        minutes -= 60
        hours += 1
    hours += (time1.hour + time2.hour)
    added_time = data.Time(hours, minutes, seconds)
    return added_time

# Part 4
def is_descending(descend_list : list[float]) -> bool:
    i = 1
    for item in descend_list:
        if item == descend_list[0]:
            continue
        if item < descend_list[i - 1]:
            i += 1
        if i == len(descend_list):
            return True
        elif item > descend_list[i - 1]:
            return False




# Part 5
def largest_between(int_list : list[int], lower : int, upper : int):
    greatest_value = 0
    if lower > upper:
        return None
    if lower < 0:
        lower = 0
    if upper > len(int_list):
        upper = (len(int_list) - 1)
    while lower < upper:
        if int_list[lower] > greatest_value:
            greatest_value = int_list[lower]
        else:
            lower += 1
    return int_list.index(greatest_value)


# Part 6
def furthest_from_origin(point_list : list[data.Point]):
    if len(point_list) == 0:
        return None
    furthest_distance = 0
    furthest_point = 0
    for point in point_list:
        deltax = abs(point.x)
        deltay = abs(point.y)
        dist = math.sqrt((deltax**2) + (deltay**2))
        if dist > furthest_distance:
            furthest_distance += dist
            furthest_point = point
        else:
            continue
    return point_list.index(furthest_point)



