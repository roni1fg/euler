# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

CHECK_LIST = [5, 7, 11, 13, 17]
NUM_DIGITS = 10
PANDIGITAL_SET = set('0123456789')

def check_pandigit(prod):
    # if len(prod) != NUM_DIGITS:
    #     print(prod)
    #     input()
    return set(prod) == PANDIGITAL_SET


def check_division(num):
    for i in range(3, NUM_DIGITS - 2):
        # print(num[i:i+3], CHECK_LIST[i-3])
        if int(num[i:i+3]) % CHECK_LIST[i-3] != 0:
            return False
    return True


def check_division_by_3(num_str):
    return sum([int(digit) for digit in num_str[2:5]]) % 3 == 0


def find_special(min_thresh, max_thresh):
    special_sum = 0
    i = int(min_thresh)
    while i < max_thresh:
        # if i > 1406357250:
        #     print(i)
        num_str = str(i)
        if num_str[0] == num_str[1]:
            i += 100000000
            print(i)
        elif num_str[1] == num_str[2]:
            i += 10000000
            # print(i)
        elif num_str[2] == num_str[3]:
            i += 1000000
            # print(i)
        elif num_str[3] == num_str[4]:
            i += 100000
        elif num_str[4] == num_str[5]:
            i += 10000
            # print(i)
        elif int(num_str[3]) % 2 != 0:
            i += 1000000
        elif not check_division_by_3(num_str):
            i += 100000
        else:
            if check_pandigit(num_str) and check_division(num_str):
                print(i)
                special_sum += i
            i += 1
    return special_sum


def main():
    # print(check_division('1406357289'))
    # print(check_division_by_3('00406'))
    # print(check_division_by_3('00217'))
    min_threshold = 9012345678
    max_threshold = 9876543210
    # max_threshold = 9876543210
    print('sum is:{}'.format(find_special(min_threshold, max_threshold)))

if __name__ == '__main__':
    main()
# numbers are
# 1406357289
# 1430952867
# 1460357289
# 4106357289
# 4130952867
# 4160357289