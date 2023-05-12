# Get the index position of the target (if found), using binary search. 
def recursive_binary_search(list, target):
    list_length = len(list)
    
    if list_length == 0:
        return False
    else:
        middle = list_length // 2

        if list[middle] == target:
            return True
        else:
            if list[middle] < target:
                return recursive_binary_search(list[middle+1:], target)
            else:
                return recursive_binary_search(list[:middle], target)
            
def verify(result):
    print("Target found:", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

result = recursive_binary_search(numbers, target)
verify(result)