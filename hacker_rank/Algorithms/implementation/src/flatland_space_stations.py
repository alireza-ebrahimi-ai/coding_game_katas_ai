"""
6 6
0 1 2 4 3 5
0

5 2
0 4
2

"""

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]


distance = []
min_dist = n
for i in range(n):
    if i in c:
        distance.append(0)
    else:
        min_dist = n
        for j in range(m):
            if min_dist > abs(i - j):
                min_dist = abs(i - j)
        distance.append(min_dist)

print(max(distance))


