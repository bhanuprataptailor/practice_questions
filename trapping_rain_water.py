# Problem Statement: Consider an array of towers with width 1 unit, Calculate the amount of water trapped. HINT: plot
# a bar chart of the given array and see the water trapped in between the towers.
def calculate_area(towers, left, right):
    area = 0
    c = left + 1
    r = right
    effective_tower = min(towers[left], towers[right])
    while c != r:
        area += effective_tower - towers[c]
        c = c + 1
    return area


def find_trapping_rain_water(towers):
    total_water = 0
    left = 0
    right = left + 1

    while right < len(towers):
        if right + 1 == len(towers):
            total_water += calculate_area(towers, left, right)
            break
        if towers[right] > towers[left]:
            total_water += calculate_area(towers, left, right)
            left = right
            right = left + 1
        else:
            right += 1
    return total_water


def visualize_array(towers):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(15, 5))
    plt.bar(range(0, len(towers)), towers, color='maroon', width=1)
    plt.xlabel("Towers")
    plt.ylabel("Height of towers")
    plt.title("Visualization of towers")
    plt.show()


towers = [0, 1, 0, 2, 1, 0, 3, 1, 4, 5, 1, 5, 2, 6, 3, 6, 2, 7]
print(find_trapping_rain_water(towers))
visualize_array(towers)  # <- Use this to visualize your solutions
