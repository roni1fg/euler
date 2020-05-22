# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?

def sum_of_digits(num):
    return sum([int(digit) for digit in str(num)])


def find_max_digit_sum(threshold):
    max_sum = 0
    for i in range(threshold):
        for j in range(threshold):
            max_sum = max(sum_of_digits(i**j), max_sum)
    return max_sum


if __name__ == '__main__':
    threshold = 101
    # print(sum_of_digits(5567))
    print(find_max_digit_sum(threshold))