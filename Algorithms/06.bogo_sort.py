import random

# Bogo Sort algo.
# A highly inefficient sorting algorithm that works by shuffling a list randomly,
# until it happens to be sorted.
def bogo_sort(list):
    attempts = 0

    while not is_sorted(list):
        random.shuffle(list)
        attempts = attempts + 1

    return list, attempts

# Check if the list is sorted.
def is_sorted(list):
    list_length = len(list)

    for index in range(list_length - 1):
        if list[index] > list[index + 1]:
            return False
    return True

numbers = [3, 9, 1, 0, 5]
result, attempts = bogo_sort(numbers)
print(result)
# [0, 1, 3, 5, 9]
print("No. of attempts:", attempts) # The number of attempts will be random at each execution.
# No. of attempts: 68