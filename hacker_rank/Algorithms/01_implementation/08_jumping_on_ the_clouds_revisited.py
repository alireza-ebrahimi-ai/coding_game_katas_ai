"""
Aerith is playing a cloud game!
In this game, there are  clouds numbered sequentially from 0 to n-1. Each cloud is either an ordinary cloud or
a thundercloud.

8 2
0 0 1 0 0 1 1 0

= 92
"""

n, k = int(input().strip().split(' '))
c = [int(c_temp) for c_temp in input().strip().split(' ')]

step = 0
pos = 0
while pos < n:
    if pos + 2 < n:
        if c[pos + 2] != 1:
            pos += 2
            step += 1
        else:
            pos += 1
            step += 1
    else:
        if pos +1 < n:
            step += 1
        pos += 1

print(step)