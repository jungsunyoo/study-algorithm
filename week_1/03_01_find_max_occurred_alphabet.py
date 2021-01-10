input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for i in string:
        if not i.isalpha():
            continue
        currind = ord(i) - ord('a')
        alphabet_occurrence_array[currind] += 1
    init_ind = 0
    init_val = 0
    for i, j in enumerate(alphabet_occurrence_array):
        if j > init_val:
            init_ind = i
    return chr(ord('a')+init_val)


result = find_max_occurred_alphabet(input)
print(result)