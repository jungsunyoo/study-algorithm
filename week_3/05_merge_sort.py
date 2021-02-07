array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    ind = len(array) // 2 # 중간값 구하
    if len(array) <= 1:
        return array
    # arr1 = array[:ind-1]
    # arr2 = array[ind:]다
    # if len(array) > 1:
    else:
        return merge(merge_sort(array[:ind]), merge_sort(array[ind:])) # if ind > 0
    # return array
# 퀴즈: 시간복잡도는?? O(N)*log2(N) -> O(NlogN) (상수  뗀 것)

def merge(array1, array2): # -> O(N)
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!