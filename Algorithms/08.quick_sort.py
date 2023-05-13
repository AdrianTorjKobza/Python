# Quick Sort algo.
# Sorting algorithm that uses a divide-and-conquer approach,
# to sort an array or a list of elements in ascending or descending order.
def quick_sort(list):
    list_length = len(list)

    if list_length <= 1:
        return list
    
    less_then_pivot = []
    greater_then_pivot = []
    pivot = list[0] # Select the first element of the list, as pivot.

    for value in list[1:]:
        if value <= pivot:
            less_then_pivot.append(value)
        else:
            greater_then_pivot.append(value)

    return quick_sort(less_then_pivot) + [pivot] + quick_sort(greater_then_pivot)

numbers = [4, 9, 0, 3, 4, 7, 1]
sorted_list = quick_sort(numbers)
print(sorted_list)
# [0, 1, 3, 4, 4, 7, 9]