# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

numbers_list = range(1, 500000)
number_str = '0' + ''.join([str(x) for x in numbers_list])
print(number_str[:30])
print(len(number_str))
product = 1
i = 1
while i <= 1000000:
    product *= int(number_str[i])
    print('i = {}'.format(i))
    i *= 10

print(product)
