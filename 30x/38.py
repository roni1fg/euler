# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


PANDIGITS_SET = set('123456789')

def check_pandigit(prod):
    return len(prod) == 9 and set(prod) == PANDIGITS_SET

def is_pandigital(num):
    i = 2
    prod_str = str(num)
    prod_num = num
    while prod_num < 987654321 and i < 9:
        prod_str += str(num*i)
        if check_pandigit(prod_str):
            print(prod_str)
            return True
        prod_num = int(prod_str)
        i += 1
    return False

def find_pandigital_mult():
    pandigital_numbers = []
    for i in range(1, 100000):
        if is_pandigital(i):
            pandigital_numbers.append(i)
    return pandigital_numbers

if __name__ == '__main__':
    # print(is_pandigital(192))
    # print(is_pandigital(193))
    # print(is_pandigital(9))
    # pandigital_list = find_pandigital_mult()
    prod_list = [918273645,192384576,219438657,273546819,327654981,672913458,679213584,692713854,726914538,729314586,732914658,769215384,792315846,793215864,926718534,927318546,932718654]
    # print(pandigital_list)
    # print('maximum number is: {}'.format(max(pandigital_list)))
    print(max(prod_list))