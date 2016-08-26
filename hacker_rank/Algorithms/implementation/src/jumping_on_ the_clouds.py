"""
Emma is playing a new mobile game involving n clouds numbered from 0 to n-1.
A player initially starts out on cloud C0,
and they must jump to cloud Cn-1. In each step, she can jump from any cloud i to cloud i+1 or cloud i+2.
7
0 0 1 0 0 1 0
= 4
"""

n = int(input().strip())
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
