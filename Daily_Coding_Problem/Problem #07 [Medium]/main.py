import string

# Initialize the alphabet as dictionary data structure.
alphabet = {}
i = 1

# Create the alphabet.
for c in string.ascii_lowercase: 
    alphabet.update({i:c})
    i=i+1

# print (alphabet) ==> {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

# The message that we need to decode.
message_coded = [2,7,1,1,5]
length = len(message_coded)

# The max amount of times the message can be decoded.
# f(1) = 1 for e.g. [1]
# f(2) = 2 for e.g. [2,1]
# f(3) = 3 for e.g. [1,1,5]
# f(4) = 5 for e.g. [1,1,1,2]
# f(5) = 8 for e.g. [2,2,1,1,4]
# The above is Fibonacci sequence. Basically the best case scenario, assuming only valid numbers between [1..26].
def count_max_solutions(n):
   if n <= 1:
       return n
   else:
       return (count_max_solutions(n-1) + count_max_solutions(n-2))

max = count_max_solutions(length+1)

# If number is < 1, set the total number of solutions = 0.
# If number is > 2 (e.g. resulting in 30, 42, 55, etc) or number is > 26, decrease the number of solutions by 1.
def count_solutions(total, length):
    for m in message_coded:
        if m < 1:
            total = 0
            return total

    l = 0    
    for l in range(length-1):
        if message_coded[l] > 2 or (message_coded[l] == 2 and message_coded[l+1] > 6):
            total = total - 1

    return total

print (count_solutions(max, length))
