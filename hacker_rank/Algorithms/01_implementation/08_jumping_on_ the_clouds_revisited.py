"""
Aerith is playing a cloud game!
In this game, there are  clouds numbered sequentially from 0 to n-1. Each cloud is either
an ordinary cloud or a thundercloud.

8 2
0 0 1 0 0 1 1 0

= 92
"""

n, k = map(int, input().strip().split(' '))
c = [int(c_temp) for c_temp in input().strip().split(' ')]

energy = 100
position = 0
while position != n:
    if c[position] == 1:
        energy -= 3
    else:
        energy -= 1
    position += k

print(energy)