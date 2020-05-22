# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
#
# 2–√=1+12+12+12+…
# By expanding this for the first four iterations, we get:
#
# 1+12=3/2=1.5
# 1+12+12=7/5=1.4
# 1+12+12+12=17/12=1.41666…
# 1+12+12+12+12=41/29=1.41379…
#
# The next three expansions are 9970, 239169, and 577408, but the eighth expansion, 1393985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
#
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

from math import log10, floor


def is_numerator_longer(numerator, denominator):
    return floor(log10(numerator)) > floor(log10(denominator))


def count_special_fractions(threshold):
    count = 0
    den = 2
    numerator = 3
    for i in range(threshold):
        if is_numerator_longer(numerator, den):
            # print(numerator, den)
            count += 1
        den = numerator + den
        numerator = 2 * den - numerator
    return count


def main():
    threshold = 1001
    print(count_special_fractions(threshold))


if __name__ == '__main__':
    main()
