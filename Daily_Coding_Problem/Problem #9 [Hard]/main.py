numbers = [2, 4, 6, 2, 5]
length = len(numbers)

# start = [0, 1]
# stop = [length]
# step = [2, 3]
# Create new lists using start, stop, step -> list (start:stop:step). The below should cover most of the cases.
numbers_non_adjacent1 = numbers [0 : length : 2]
numbers_non_adjacent2 = numbers [0 : length : 3]
numbers_non_adjacent3 = numbers [1 : length : 2]

def largest_sum():
    total_list = []

    n, total = 0, 0
    for n in numbers_non_adjacent1:
        total = total + n
        total_list.append(total)
    
    n, total = 0, 0
    for n in numbers_non_adjacent2:
        total = total + n
        total_list.append(total)

    n, total = 0, 0
    for n in numbers_non_adjacent3:
        total = total + n
        total_list.append(total)

    return max (total_list)

print (largest_sum())
