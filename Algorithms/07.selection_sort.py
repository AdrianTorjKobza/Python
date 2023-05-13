# Selection Sort algo.
# Sorting algorithm that works by repeatedly finding the minimum element,
# from an unsorted portion of an array and moving it to the beginning of the sorted portion.
def selection_sort(list):
    sorted_list = []
    list_length = len(list)

    for i in range(0, list_length):
        index_to_move = index_of_min(list)
        min_index = list.pop(index_to_move)
        sorted_list.append(min_index)
    
    return sorted_list


def index_of_min(list):
    min_index = 0
    list_length = len(list)

    for i in range (1, list_length):
        if list[i] < list[min_index]:
            min_index = i
    
    return min_index

numbers = [9, 2, 5, 1, 0, 7]
result = selection_sort(numbers)
print(result)
# [0, 1, 2, 5, 7, 9]
