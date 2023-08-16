# Statement: consider each value in the array as a tower of negligible width, calculate the max area, the distance
# between the towers is the difference between their indices.

# test_case 1:
#    towers = [4, 8, 1, 2, 3, 9], output = 8*4 = 32
# test_case 2:
#     towers = [1, 3, 4, 6, 5], output = 3 * 3 = 9
# test_case 3:
#     towers = [9, 8, 15, 0, 1, 3, 7, 10, 9], output = 72

def find_max_area(towers):
    left_pointer = 0
    right_pointer = len(towers) - 1
    max_area = 0

    while left_pointer != right_pointer:
        calculate_area = min(towers[left_pointer], towers[right_pointer]) * (right_pointer - left_pointer)
        if calculate_area > max_area:
            max_area = calculate_area
        if towers[left_pointer] < towers[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1

    return max_area


towers = [9, 8, 15, 0, 1, 3, 7, 10, 9]
print(find_max_area(towers))
