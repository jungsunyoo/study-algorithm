input = 20


def find_prime_list_under_number(number):
    prime_list = []
    for i in range(2, number+1, 1):  # loops over 2 to number incrementally by 1
        rem = 0
        for j in range(1, i+1, 1):  # 다음 for loop에서 remainder가 0인게 자기 자신 밖에 없어야함
            if i % j == 0:
                rem += 1
        if rem == 2:
            prime_list.append(i)
    return prime_list

# 시간 복잡도: O(n^2)

result = find_prime_list_under_number(input)
print(result)

##############++++++++++++++++++++++++++++
# Tutor's code:

input = 20

# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다.
# 착안점 2: 주어진 자연수 N이 소수이기 위한 필요충분 조건은
# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘 중 하나는
# 반드시 N의 제곱근 이하 (예를 들면 20이면 19로 나눠볼 필요 없다)
def find_prime_list_under_number(number):
    prime_list = []
    for i in range(2, number+1):  # loops over 2 to number+1 incrementally by 1
        for j in range(2,i):  # 2 ~ i-1 // 비효율적인 방법! 왜냐하면 예를들면 6이면 2,3으로 나눠지기때문에 생각해볼것도 없음 ->
            # 착안점 1: prime list인 애들로만 나눠봐도 된다 (for j in prime_list: 로 바꾸는게 더 효율적인 알고리즘)
            if i % j == 0: # 착안점 2 반영된 개선코드: if i % j == 0 and j * j <= i:
                break # 이 숫자는 소수가 아니
        else: # break되지 않는다면
            prime_list.append(i)
    return prime_list

# 시간 복잡도: O(n^2)

result = find_prime_list_under_number(input)
print(result)

# 알고리즘은 어떤 식으로든 개선할 수 있다
# 알고리즘을 개선하기 위해서는 특정 문제의 특징을 떠올리면 좋다 (예를 들면 소수의 특징)
# 어떻게 하면 개선할 수 있는지 고민해보는 습관