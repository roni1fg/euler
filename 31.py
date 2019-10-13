money_list = [1, 2, 5, 10, 20, 50, 100, 200]
test_list = [5, 2, 1]
money_list = money_list[::-1]
WANTED_SUM = 10


def check_list(money, wanted):
    pass


def print_option(money_list, i, j, k):
    print('{coin1} : {cnt1}\t{coin2} : {cnt2}\t{coin3} : {cnt3}'.format(coin1=money_list[0], coin2=money_list[1], coin3=money_list[2], cnt1=i, cnt2=j, cnt3=k))

def add_solution(solutions, money_list, i, j, k):
    if [i, j, k] not in solutions:
        solutions.append([i, j, k])
        print_option(money_list, i, j, k)

def main():
    counter = 0
    i, j, k = (0, 0, 0)
    solutions = []
    # for coin in test_list:
    temp_sum1 = int(WANTED_SUM / test_list[0])
    for i in range(temp_sum1, -1, -1):
        if i * test_list[0] == WANTED_SUM:
            add_solution(solutions, test_list, i, j, k)
        temp_sum2 = int(WANTED_SUM / test_list[1])
        for j in range(temp_sum2, -1, -1):
            if i * test_list[0] + j * test_list[1] == WANTED_SUM:
                add_solution(solutions, test_list, i, j, k)
            temp_sum3 = int(WANTED_SUM / test_list[2])
            for k in range(temp_sum3, -1, -1):
                if i * test_list[0] + j * test_list[1] + k * test_list[2] == WANTED_SUM:
                    add_solution(solutions, test_list, i, j, k)

    print('counter: {num}'.format(num=len(solutions)))


if __name__ == '__main__':
    main()
