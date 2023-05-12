# Get the index position of the target (if found), using linear search. 
def linear_search(list, target):
    list_length = len(list)

    for index in range(0, list_length):
        if list[index] == target:
            return index        

    return None

def verify(index, target):
    if index is None:
        print("Target", target, "not found in the list.")
    else:
        print("Target", target, "found at index", index, "in the list.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

result = linear_search(numbers, target)
verify(result, target)