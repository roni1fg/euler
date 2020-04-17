# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

PANDIGITS_SET = set('123456789')

def check_pandigit(mcand, mplier, prod):
    my_str = str(mcand) + str(mplier) + str(prod)
    return len(my_str) == 9 and set(my_str) == PANDIGITS_SET

def find_multiplier_1():
    results = []
    for i in range(1, 10):
        for j in range(1234, 9877):
            if check_pandigit(i,  j, i*j):
                print('{i} * {j} = {res}'.format(i=i, j=j, res=i*j))
                results.append(i * j)
    print('Done checking 1 digit')
    return results

def find_multiplier_2():
    results = []
    for i in range(12, 99):
        for j in range(123, 835):
            if check_pandigit(i,  j, i*j):
                print('{i} * {j} = {res}'.format(i=i, j=j, res=i*j))
                results.append(i*j)
    print('Done checking 2 digit')
    return results

def calc_sum_pandigits():
    products = []
    products = find_multiplier_1() + find_multiplier_2()
    print('sum of products is {}'.format(sum(set(products))))


if __name__ == '__main__':
    calc_sum_pandigits()