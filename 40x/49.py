# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
#   (i) each of the three terms are prime, and,
#   (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?
import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def find_primes(start_num, end_num):
    return [x for x in range(start_num, end_num, 2) if is_prime(x)]

def is_permutation(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))

def find_special_numbers(prime_list):
    permutations = []
    for i, prime in enumerate(prime_list):
        permutations.append([prime])
        for prime2 in prime_list[i+1:]:
            if is_permutation(prime, prime2):
                permutations[i].append(prime2)
                prime_list.remove(prime2)
    return [perm_list for perm_list in permutations if len(perm_list) > 2]

def find_const_diff(permutations):
    for perm_list in permutations:
        for i, num in enumerate(perm_list):
            for num2 in perm_list[i+1:]:
                if (2*num2 - num) in perm_list:
                    print(num, num2, 2*num2 - num)

def main():
    start = 1001
    end = 10000
    prime_list = find_primes(start, end)
    # print(len(prime_list))
    permutations = find_special_numbers(prime_list)
    print(permutations[:10])
    print(len(permutations))
    find_const_diff(permutations)

if __name__ == '__main__':
    main()