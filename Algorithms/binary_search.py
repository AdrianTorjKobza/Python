# Get the index position of the target (if found), using binary search. 
def binary_search(list, target):
    first = 0

    list_length = len(list)
    last = list_length - 1
    
    while first <= last:
        middle = (first + last) // 2 
        
        if list[middle] == target:
            return middle
        elif list[middle] < target:
            first = middle + 1
        else:
            last = middle - 1

    return None

def verify(index, target):
    if index is None:
        print("Target", target, "not found in the list.")
    else:
        print("Target", target, "found at index", index, "in the list.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

result = binary_search(numbers, target)
verify(result, target)