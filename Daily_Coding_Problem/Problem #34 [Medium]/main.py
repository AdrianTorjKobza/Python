string = "google"
string_palindrom = string

def check_if_palindrom (str):
    reversed_str = ''.join(reversed(str))

    if str == reversed_str:
        return 1

    return 0

n = -1

while check_if_palindrom(string_palindrom) == 0:
    string_palindrom = string

    for i in range(n, 0, 1):
        string_palindrom = string[i] + string_palindrom
    
    n = n - 1

print (string_palindrom)
