# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def is_permutation(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))


def scan_numbers():
    ten_power = 2
    current_num = 10 ** ten_power
    while True:
        while current_num <= (10 ** (ten_power + 1)) / 6:
            if is_permutation(current_num, current_num * 2) and is_permutation(current_num, current_num * 3) and \
                    is_permutation(current_num, current_num * 4) and is_permutation(current_num, current_num * 5) \
                    and is_permutation(current_num, current_num * 6):
                return current_num
            current_num += 1
        ten_power += 1
        print('ten_power:', ten_power)

if __name__ == '__main__':
    winner = scan_numbers()
    for i in range(1, 7):
        print(winner * i)
