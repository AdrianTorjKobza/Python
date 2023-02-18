array = [10, 5, 2, 7, 8, 7]
k = 3

lists_of_lists = []
sublist = []

def split_list (array, k):
    for i in range(k):
        sublist.append(array[i])
    
    return sublist

while len(array) >= k:
    split_list(array, k)
    lists_of_lists.append(sublist)
    array.pop(0)
    sublist = []

for i in range(len(lists_of_lists)):
    print (max(lists_of_lists[i]))
