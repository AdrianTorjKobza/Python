numbers = [0,2,3,5]
numbers.sort()

def missing_positive_integer():
    missing_number = 0
    i = 0

    for _ in numbers:
        if i == len(numbers)-1:
            missing_number = numbers[i] + 1
            return missing_number
            
        elif numbers[i] >= 0 and numbers[i+1] - numbers[i] > 1:
            missing_number = numbers[i] + 1
            return missing_number
            
        else:
            i = i + 1

print (missing_positive_integer())
