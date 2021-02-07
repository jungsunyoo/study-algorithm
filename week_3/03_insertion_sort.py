input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    # 이 부분을 채워보세요!
    for curr_ind in range(1, len(array)):
        # curr_ind = i+1
        counter = True
        while counter:
            if curr_ind > 0 and array[curr_ind] < array[curr_ind - 1]:
                array[curr_ind], array[curr_ind - 1] = array[curr_ind - 1], array[curr_ind]
                curr_ind -= 1
            else:
                counter = False
    return array

insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!


# Teacher's code: Use for loop

def insertion_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)
    for i in range(1,n):
        for j in range(i):
            # print(i-j) -> 원하는 인덱스 나온다
            if array[i - j - 1] > array[i-j]:
                array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
            else:
                break
    return array
# Time complexity: O(N^2), but because of break, omega(N)