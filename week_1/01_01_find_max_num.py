input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    left = array[0]
    for i in range(len(array) - 1):
        if array[i] > left:
            left = array[i]
    return left


# or (튜터님 해법)
# def find_max_num(array):
#     for num in array:
#          for compare_num in arrray:
#              if num < compare_num:
#                  break
#          else:
#              return num

result = find_max_num(input)
print(result)
