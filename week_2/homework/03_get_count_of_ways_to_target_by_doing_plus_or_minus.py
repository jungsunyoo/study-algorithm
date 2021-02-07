numbers = [1, 1, 1, 1, 1]
target_number = 3


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    if (target % 2 != len(array) % 2) or (target > 5 or target < -5):
        return print("반환할 수 없습니다")
    else:
        return factorial(len(array)) / factorial(target+1) * factorial(len(array) - target-1)


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
