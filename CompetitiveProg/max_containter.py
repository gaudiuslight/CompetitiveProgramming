# algorithm used: 2 shifting pointers
def get_max_area_container(list_of_heights):
    if not list_of_heights or len(list_of_heights) == 1:
        return 0
    
    p1 = 0
    p2 = len(list_of_heights) - 1
    max_area = 0
    while p1 < p2:
        height = min([list_of_heights[p1], list_of_heights[p2]])
        area = height * (p2 - p1)
        max_area = max([max_area, area])
        if list_of_heights[p1] <= list_of_heights[p2]:
            p1 += 1
        else:
            p2 -= 1
    return max_area

print(get_max_area_container([4,8,1,2,3,9]))