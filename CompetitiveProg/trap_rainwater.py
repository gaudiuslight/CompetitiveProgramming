"""
Given an array of integers representing an elevation 
map where the width of each bar is 1,
return how many rainwater it can trap
"""
sample = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]

def brute_force(heights):
    total_water = 0
    for p in range(len(heights)):
        left_p = right_p = p
        max_left = max_right = 0
        while left_p >= 0:
            max_left = max(max_left, heights[left_p])
            left_p -= 1
        while right_p < len(heights):
            max_right = max(max_right, heights[right_p])
            right_p += 1
        current_water = min(max_left, max_right) - heights[p]
        if current_water >= 0:
            total_water += current_water
    return total_water

print(brute_force(sample))
        
def optimal_solution(heights):
    left_p, right_p = 0, len(heights) - 1
    max_left = max_right = 0
    total_water = 0
    while left_p < right_p:
        if heights[left_p] <= heights[right_p]:
            if heights[left_p] >= max_left:
                max_left = heights[left_p]
            else:
                total_water += (max_left - heights[left_p])
            left_p += 1
        else:
            if heights[right_p] >= max_right:
                max_right = heights[right_p]
            else:
                total_water += (max_right - heights[right_p])
            right_p -= 1
    return total_water

print(optimal_solution(sample))





