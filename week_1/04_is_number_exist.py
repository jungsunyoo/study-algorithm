input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for i in array: # array 길이만큼 아래 연산 실행된다
        if number == i: # 비교 연산 1번 실행
            return True # 총 시간복잡도:  N * 1 = N만큼
    return False


result = is_number_exist(3, input)
print(result)