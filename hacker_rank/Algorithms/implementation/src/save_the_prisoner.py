"""

A jail has N prisoners, and each prisoner has a unique id number,
S, ranging from 1 to N. There are M sweets that must be distributed to the prisoners.

1
5 3 5

= 2
"""

t = int(input().strip())
num_cons = []
num_sweet = []
start_arr = []
for i in range(0, t):
    n, m, s = input().strip().split(' ')
    num_cons.append(int(n))
    num_sweet.append(int(m))
    start_arr.append(int(s))

for i in range(0, t):
    position = (start_arr[i] + num_sweet[i] - 1) % num_cons[i]
    if position == 0:
        print(num_cons[i])
    else:
        print(position)







