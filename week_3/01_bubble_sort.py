input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    for l in range(len(array) - 1): # n의 길이만큼 반복
        counter = len(array) - l - 1
        for i in range(counter):    # n의 길이만큼 반복
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array

# 시간복잡도는 O(N^2)

bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!