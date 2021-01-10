def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for i in string:
        if not i.isalpha():
            continue
        # else:
        currind = ord(i) - ord('a')
        alphabet_occurrence_array[currind] += 1


    # 이 부분을 채워보세요!

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))