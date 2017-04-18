import math
from itertools import combinations


def calc(r, k):
    pi = math.pi

    combi_list = []
    combi_list.extend(combinations(r, k + 1))
    comparator_sum = 0
    for tuple_id in combi_list:
        tuple_sum = sum(tuple_id)

        missing_r = []
        if k != n - 1:
            for element in r:
                if element not in tuple_id:
                    missing_r.append(element ** 2 * pi)
        comparator_sum += tuple_sum ** 2 * pi + sum(missing_r)
    print(comparator_sum / len(combi_list))


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
r = list(map(int, input().strip().split(' ')))

calc(r, k)



