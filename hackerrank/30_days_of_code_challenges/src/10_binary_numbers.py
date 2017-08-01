"""
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum
number of consecutive 1's in n's binary representation.

"""

n = int(input().strip())

n_binary = str(bin(n))[2:]
count = 0
max_count = 0

for i in range(0, len(n_binary)):
    if n_binary[i] == '1':
        count += 1
    else:
        if max_count < count:
            max_count = count
        count = 0

if max_count < count:
    print(count)
else:
    print(max_count)
