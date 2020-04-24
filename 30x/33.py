# he fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


def check_case(nom, denom):
    result = nom / denom
    a = nom % 10
    b = denom % 10
    c = nom // 10
    d = denom // 10
    if nom % 10 == 0 or denom % 10 == 0:
        return
    if (c == d) and (a / b) == result \
        or (c == b) and (a / d) == result \
        or (a == d) and (c / b) == result \
        or (a == b) and (c / d) == result:
            print('nom: {nom}, denominator: {denom}'.format(nom=nom, denom=denom))


def check_cases():
    for i in range(10, 100):
        # if i % 10 == 0:
            # print('Start checking i={}'.format(i))
        for j in range(10, i):
            check_case(j, i)
    print("Done")


def main():
    # check_case(45, 98)
    check_cases()

if __name__ == '__main__':
    main()