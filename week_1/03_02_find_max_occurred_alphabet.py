input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for i in string:
        if not i.isalpha():
            continue
        # else:
        currind = ord(i) - ord('a')
        alphabet_occurrence_array[currind] += 1
    max_occurence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurence = alphabet_occurrence_array[index]
        if alphabet_occurence > alphabet_occurrence_array[max_alphabet_index]:
            max_alphabet_index  = index
            max_occurence = alphabet_occurence

    return chr(ord('a')+max_alphabet_index)


result = find_max_occurred_alphabet(input)
print(result)