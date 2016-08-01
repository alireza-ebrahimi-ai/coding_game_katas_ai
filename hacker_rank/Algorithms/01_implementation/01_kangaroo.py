"""
There are two kangaroos on an x-axis ready to jump in the positive direction

"""

import math

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

if (v2 - v1 == 0) and (x1 != x2):
    print('NO')
else:
    jump = (x1 - x2) / (v2 - v1)
    if (jump >= 0) and (math.modf(jump)[0] == 0):
        print('YES')
    else:
        print('NO')





