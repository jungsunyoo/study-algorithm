input = [4, 6, 2, 9, 1]

# my code
def selection_sort(array):
    # 이 부분을 채워보세요!
    for i in range(len(array)-1):
        min_val = array[i]
        min_ind = i
        for j in range(i+1, len(array)):
            if min_val > array[j]:
                min_val = array[j]
                min_ind = j
        array[i], array[min_ind] = array[min_ind], array[i]
    return array
selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

# Teacher's code
input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(n-i):
            if array[i+j] < array[min_index]:
                min_index = i+j
        array[i], array[min_index] = array[min_index], array[i]
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

# 시간복잡도는 O(N^2)