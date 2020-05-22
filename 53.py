# There are exactly ten ways of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, (53)=10.
#
# In general, (nr)=n!r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.
#
# It is not until n=23, that a value exceeds one-million: (2310)=1144066.
#
# How many, not necessarily distinct, values of (nr) for 1≤n≤100, are greater than one-million?

def factorial(num):
    if num <= 1:
        return 1
    return factorial(num - 1) * num

def get_factorials_list(threshold):
    return [factorial(n) for n in range(threshold + 1)]

def calc_combinations(n, r, fact_list):
    return fact_list[n] / (fact_list[r] * fact_list[n-r])

def scan_range(threshold, fact_list, compare_thresh):
    counter = 0
    for n in range(1, threshold + 1):
        for r in range(n+1):
            if calc_combinations(n, r, fact_list) > compare_thresh:
                counter += 1
    return counter

def main():
    threshold = 100
    test_num = 0
    compare_threshold = 1000000
    # print(factorial(test_num))
    fact_list = get_factorials_list(threshold)
    print(fact_list[:7])
    # print(calc_combinations(23, 10, fact_list))
    print('count of numbers greater then {threshold} is {result}'.\
          format(threshold=compare_threshold, result=scan_range(threshold, fact_list, compare_threshold)))


if __name__ == '__main__':
    main()