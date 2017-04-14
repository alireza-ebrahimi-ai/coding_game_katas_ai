import math
from itertools import combinations

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
r = list(map(int, input().strip().split(' ')))

Pi = math.pi

combi_list = []
combi_list.extend(combinations(r, k + 1))

print(combi_list)



