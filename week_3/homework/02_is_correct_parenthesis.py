s = "(())()"

def assign_value(string):
    if string == '(':
        return 1
    elif string == ')':
        return -1
    else:
        return "Error: please only enter parentheses"

def is_correct_parenthesis(string):
    # 구현해보세요!
    sum = 0
    for i in string:
        sum += assign_value(i)
        if sum < 0:
            return False
    if sum is not 0:
        return False
    else:
        return True
    # return


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!