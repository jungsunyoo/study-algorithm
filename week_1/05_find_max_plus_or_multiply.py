input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    addOne = False
    addZero = False
    multiply_base = 1

    for i in array:
        if i == 1:
            addOne = True
        elif i == 0:
            addZero = True
        else:
            multiply_base *= i
    if addOne:
        multiply_base += 1
    if addZero:
        multiply_base += 0
    return multiply_base


result = find_max_plus_or_multiply(input)
print(result)

# Tutor's code:

# def find_max_plus_or_multiply(array):
#     multiply_sum = 0
#     for number in array:
#         if number <= 1 or multiply_sum <= 1:
#             multiply_sum += number
#         else:
#             multiply_sum *= number
#     return multiply_sum
# ans = 728

# 페이스북 기출문제