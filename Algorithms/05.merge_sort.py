# Merge Sort algo.
# Sorting algorithm that uses the divide-and-conquer approach.
# It works by dividing an array into two halves, sorting each half recursively,
# and then merging the sorted halves back together to form a fully sorted array.
def merge_sort(list):
    list_length = len(list)

    if list_length <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

# Dive the list into half. Returns two sublists: left and right.
def split(list):
    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]

    return left, right

def merge(left, right):
    left_length = len(left)
    right_length = len(right)
    l = []
    i = 0
    j = 0

    while i < left_length and j < right_length:
        if left[i] < right[j]:
            l.append(left[i])
            i = i + 1
        else:
            l.append(right[j])
            j = j + 1

    # Case when the right list is shorter then the left list.
    while i < left_length:
        l.append(left[i])
        i = i + 1

    # Case when the left list is shorter then the right list.
    while j < right_length:
        l.append(right[j])
        j = j + 1

    return l

numbers = [2, 10, 6, 1, 7, 5, 4, 0]
result = merge_sort(numbers)
print(result)
# [0, 1, 2, 4, 5, 6, 7, 10]
