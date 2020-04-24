# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?
import math

def find_solutions(p):
    num_solutions = 0
    for a in range(1, int(p/3) + 1):
        for b in range(a, int(p/2) + 1):
            if (a + b + math.sqrt(a**2 + b**2)) == p:
                num_solutions += 1
    return num_solutions

def check_p_values(threshold):
    solutions = {}
    for i in range(threshold + 1):
        if i % 50 == 0:
            print(i)
        solutions[i] = find_solutions(i)
    return solutions

def find_max_solutions(solutions):
    max_soltions = 0
    max_p = 0
    for key, value in solutions.items():
        if value > max_soltions:
            max_p = key
    return max_p

if __name__ == '__main__':
    threshold = 1000
    # print(find_solutions(120))
    solutions = check_p_values(threshold)
    print(solutions)
    print('Done finding solutions')
    print(find_max_solutions(solutions))

# 420 : 5
# 840: 8