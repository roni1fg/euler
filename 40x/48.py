# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def find_num(threshold):
    return sum([x**x for x in range(1, threshold+1)])

def main():
    threshold = 1000
    print(str(find_num(threshold))[-10:])

if __name__ == '__main__':
    main()

