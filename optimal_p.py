from math import factorial, ceil

START = 0,0,0,0
GOAL = 12,11,8,7

def n(e, ep, eo, c, cp, co):
    return ceil((2 ** eo) * (3 ** co) \
         * (factorial(e) / factorial(e - ep)) \
         * (factorial(c) / factorial(c - cp)) \
         / (2 if (e == ep or c == cp) else 1))

def total_n(ep, eo, cp, co):
    return int(n(12 - START[0], ep, eo, 8 - START[2], cp, co) \
             + n(12 - START[0] - ep, GOAL[0] - START[0] - ep, GOAL[1] - START[1] - eo,
                  8 - START[2] - cp, GOAL[2] - START[2] - cp, GOAL[3] - START[3] - co))

if __name__ == '__main__':
    combinations = []
    for ep in range(GOAL[0] - START[0] + 1):
        for eo in range(GOAL[1] - START[1] + 1):
            for cp in range(GOAL[2] - START[2] + 1):
                for co in range(GOAL[3] - START[3] + 1):
                    combinations.append(((ep, eo, cp, co),
                        (n(12 - START[0], ep, eo, 8 - START[2], cp, co),
                         n(12 - START[0] - ep, GOAL[0] - START[0] - ep, GOAL[1] - START[1] - eo,
                            8 - START[2] - cp, GOAL[2] - START[2] - cp, GOAL[3] - START[3] - co))))
    combinations.sort(key=lambda x: sum(x[1]), reverse=True)
    for x in combinations:
        print('{}\t{} cases  \t{} total'.format(x[0], x[1][0], sum(x[1])))
