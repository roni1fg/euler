# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def find_primes(start_num, end_num):
    return [2] + [x for x in range(start_num, end_num, 2) if is_prime(x)]

def find_consecutive_sum(prime_list):
    for i in range(544, 200, -1):
        for j in range(len(prime_list) - i):
            if is_prime(sum(prime_list[j:j+i])):
                print('Found: start index: {j}, len list: {i}, sum:{prime}'.format(j=j, i=i, prime = sum(prime_list[j:j+i])))
                return


def main():
    prime_list = find_primes(3, 1000000)
    print(len(prime_list))
    find_consecutive_sum(prime_list)


if __name__ == '__main__':
    main()


# 350 - 379667
# 935507
# 978001
# 978037