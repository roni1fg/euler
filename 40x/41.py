# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

import math

PANDIGITS_SET = set('123456789')


def check_pandigit(prod, num_digits):
    return len(prod) == num_digits and set(prod) == set(''.join([str(x) for x in range(1, num_digits + 1)]))


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def find_numbers(min_threshold, max_threshold, num_digits):
    for x in range(max_threshold, min_threshold - 1, -2):
        if is_prime(x) and check_pandigit(str(x), num_digits):
            return x
    return -1


def main():
    for i in range(7, 3, -1):
        max_threshold = int(''.join([str(x) for x in range(i, 0, -1)]))
        min_threshold = int(''.join([str(x) for x in range(1, i+1)]))
        print('i={}'.format(i))
        # print(min_threshold, max_threshold)
        special = find_numbers(min_threshold, max_threshold, i)
        if special != -1:
            print('Found!', special)
            # return
    print('Done')


if __name__ == '__main__':
    main()

# i=7
# Found! 7652413
