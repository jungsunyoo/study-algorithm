shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

def selection_sort_maxmin(array):
    # 이 부분을 채워보세요!
    n = len(array)
    for i in range(n-1):
        max_index = i
        for j in range(n-i):
            if array[i+j] > array[max_index]:
                max_index = i+j
        array[i], array[max_index] = array[max_index], array[i]
    return array

def get_max_discounted_price(prices, coupons):
    sorted_prices = selection_sort_maxmin(shop_prices)
    sorted_coupons = selection_sort_maxmin(coupons)
    total_price = 0
    for i, coupon in enumerate(sorted_coupons):
        total_price += (1 - coupon/100) * sorted_prices[i]

    return total_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.