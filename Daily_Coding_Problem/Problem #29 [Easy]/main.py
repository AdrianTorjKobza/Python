# Encoding.
string = "AAAABBBCCDAA"

encoded_string = ""
count = 0
i = 0

for s in string:
    compare_char = string[i]

    if s == compare_char:
        count = count + 1
    else:
        encoded_string = encoded_string + str(count) + string[i]
        i = i + count
        count = 1

encoded_string = encoded_string + str(count) + string[i]

print (encoded_string)

# Decoding.
string = "4A3B2C1D2A"

decoded_string = ""

for n in range(0, len(string), 2):
    for _ in range(int(string[n])):
        decoded_string = decoded_string + (string[n+1])

print (decoded_string)
