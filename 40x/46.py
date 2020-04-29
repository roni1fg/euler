# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
import math
import time
MAGIC_SCALAR = 2


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def get_prime_list(threshold):
    return [2] + [x for x in range(3, threshold + 1, 2) if is_prime(x)]

def find_odd_composite(start_val, threshold, prime_list):
    for odd in range(start_val, threshold + 1, 2):
        if odd % 501 == 0:
            print('checking {odd}'.format(odd=odd))
        if not(is_prime(odd)):
            flag = False
            for prime in prime_list:
                if prime > odd:
                    break
                for num in range(odd):
                    if odd == prime + MAGIC_SCALAR * (num**2):
                        # print('{odd} = {prime} + 2 * {num} ^ 2'.format(odd=odd, prime=prime, num=num))
                        flag = True
                    if flag:
                        break
                if flag:
                    break
            if not flag:
                print('the number {odd} is what you are looking for'.format(odd = odd))
                return

def main():
    start = time.time()
    prime_list = get_prime_list(6000)
    # print(prime_list[-1])
    start_val = 5001
    threshold = 6000
    find_odd_composite(start_val, threshold, prime_list)
    print("Done searching!")

    print('Run time: {num_seconds} seconds'.format(num_seconds=time.time() - start))


if __name__ == '__main__':
    main()

#check
# 0 - 3000
# 3000 - 5000
# found 5777
