"""
6 6
0 1 2 4 3 5
0

5 2
0 4
2

"""
import math

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

mean_distance = []
c.sort()

if len(c) < 2:
    mean_distance.append(abs(0 - c[0]))
    mean_distance.append(abs(n - c[0] - 1))
    print(math.floor(max(mean_distance)))
else:
    if c[0] != 0:
        mean_distance.append(round(abs(0 - c[0])))
    for i in range(0, len(c) - 1):
        mean_distance.append(round(abs(c[i] - c[i + 1])) / 2)
    if c[len(c) - 1] != n:
        mean_distance.append(round(abs(n - c[len(c) - 1] - 1)))
    print(math.floor(max(mean_distance)))




