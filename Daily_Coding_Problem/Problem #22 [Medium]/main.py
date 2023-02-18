import itertools

words = ["bed", "bath", "bedbath", "and", "beyond"]
string = "bedbathandbeyond"

# Naive solution
output_list = []
word = ""

for s in string:
    word = word + s

    if word in words:
        output_list.append(word)
        word = ""

print (output_list)

# Complete solution
all_words_combinations = []
output_list = []

for n in range(len(words) + 1):
    words_combination = itertools.permutations(words, n)
    all_words_combinations = all_words_combinations + list(words_combination)

for c in all_words_combinations:
    if ''.join(c) == string:
        output_list.append(list(c))

print (output_list)
