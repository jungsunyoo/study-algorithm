input = [3, 5, 6, 1, 2, 4]
# 지정 변수 (내가 짠 해법이랑 비슷)
# max_num = 5


def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    # 이 부분을 채워보세요!
    return max_num


result = find_max_num(input)
print(result)

# 맥: cntrl + shift + R 누르면 바로 실행