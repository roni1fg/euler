WANTED_SUM = 200


def count_ways(target):
    ways = 0
    for i in range(target, -1, -200):
        for j in range(i, -1, -100):
            for k in range(j, -1, -50):
                for l in range(k, -1, -20):
                    for m in range(l, -1, -10):
                        for n in range(m, -1, -5):
                            for o in range(n, -1, -2):
                                ways += 1
    return ways


def main():
    print('number of ways is: {}'.format(count_ways(WANTED_SUM)))


if __name__ == '__main__':
    main()
