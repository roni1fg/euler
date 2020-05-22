# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
# Not all numbers produce palindromes so quickly. For example,
#
# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
#
# That is, 349 took three iterations to arrive at a palindrome.
#
# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
#
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
#
# How many Lychrel numbers are there below ten-thousand?
#
# NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

def reverse_and_add(num):
    return num + int(str(num)[::-1])

def is_palindrom(num):
    return str(num) == str(num)[::-1]

def scan_numbers(threshold, num_iterations):
    lychrel_count = 0
    for i in range(threshold):
        lychrel_flag = True
        current_num = i
        for j in range(num_iterations):
            current_num = reverse_and_add(current_num)
            if is_palindrom(current_num):
                lychrel_flag = False
                break
        if lychrel_flag:
            lychrel_count += 1
            print('{num} is a lychrel number'.format(num=i))
    return lychrel_count


def main():
    threshold = 10000
    num_itereations = 50
    print('There are {lychrel_numbers_count} lychrel numbers until {threshold}'.\
          format(lychrel_numbers_count=scan_numbers(threshold, num_itereations), threshold=threshold))

if __name__ == '__main__':
    main()