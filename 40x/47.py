# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

import math
MAGIC = 4

def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def find_primes(start_num, end_num):
    return [2] + [x for x in range(start_num, end_num, 2) if is_prime(x)]

def find_factors(num, prime_list):
    return [prime for prime in prime_list if num % prime == 0]

def find_consecutives(start_number, prime_list, threshold):
    result = {}
    for num in range(start_number, threshold):
        factors = []
        for i in range(MAGIC):
            factor_temp = find_factors(num+i, prime_list)
            if len(factor_temp) == MAGIC:
                factors.append(factor_temp)
        if len(factors) == MAGIC:
            result[num] = factors
    return result

def is_distinct(consecutive_dict):
    pass

def main():
    prime_list = find_primes(3, 10000)
    threshold = 200000
    start = 100000
    cons_dict = find_consecutives(start, prime_list, threshold)
    print(len(cons_dict))
    print(cons_dict)



if __name__ == '__main__':
    main()