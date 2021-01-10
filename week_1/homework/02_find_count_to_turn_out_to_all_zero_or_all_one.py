input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    ndiff = 0
    flips = 0
    for i in range(len(string)-1):
        if int(string[i]) != int(string[i+1]): # difference occurred
            ndiff += 1
    if ndiff % 2 == 0:
        flips = ndiff / 2
    else:
        flips = (ndiff+1)/2
    return int(flips)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)