# Naive solution, assuming that the first and last element, are the first two tallest walls.
walls = [3, 0, 1, 3, 0, 5]

# Get the second heighest wall.
if walls[0] < walls[-1]:
    second_height = walls[0]
else:
    second_height = walls[-1]

# Remove the first and last wall.
walls.pop(0)
walls.pop(-1)

total_water = second_height * len(walls) - sum(walls)

print (total_water)

# Complete solution.
walls = [3, 0, 1, 5, 0, 5]
lists_of_lists = []

# Split the list into multiple lists.
# Input: [3, 0, 1, 5, 0, 5]
# Outout: [[3, 0, 1, 5], [5, 0, 5]]
def split_list(walls):
    sublist = []
    max = walls[0]

    for w in walls:
        if max >= w:
            sublist.append(w)
        else:
            sublist.append(w)
            lists_of_lists.append(sublist)
            sublist = []
            sublist.append(w)

    return lists_of_lists

split_list(walls)

# Return the total amount of water, for each sublist.
def get_total_water (subwall):
    if subwall[0] < subwall[-1]:
        second_height = subwall[0]
    else:
        second_height = subwall[-1]

    # Remove the first and last wall.
    subwall.pop(0)
    subwall.pop(-1)

    return (second_height * len(subwall) - sum(subwall))

# Sum the total amount of water for each sublist. 
total_water = 0
for i in lists_of_lists:
    total_water = total_water + get_total_water(i)

print (total_water)
