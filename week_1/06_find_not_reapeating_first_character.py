input = "abacabade"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    # memoization??
    empty = [0]*len(string)
    first_nonrepeat=[]
    for i in range(len(string)):
        for j in range(len(string)):
            if string[i] == string[j]:
                empty[i] += 1
    for i in range(len(empty)):
        if empty[i] == 1:
            first_nonrepeat = string[i]
            break


    return first_nonrepeat

# 시간복잡도: O(N^2 + N) or O(N(N+1))
result = find_not_repeating_character(input)
print(result)


# 강사쌤 정답: 02_find_alphabet_occurence.py 응

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for i in string:
        if not i.isalpha():
            continue
        # else:
        currind = ord(i) - ord('a')
        alphabet_occurrence_array[currind] += 1
    non_repeating_character_array=[]
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurence = alphabet_occurrence_array[index]
        if alphabet_occurence == 1:
            non_repeating_character_array.append(chr(index+ord("a")))
    print(non_repeating_character_array) # 기존 문자열의 순서를 보장해주지 않는

    for char in string:
        if char in not_repeating_character_array:
            return char
    # 이 부분을 채워보세요!

    return alphabet_occurrence_array