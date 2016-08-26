"""
You are given an array of  integers, and a positive integer.

"""

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

k_number = 0
for i in range(0, n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % k == 0:
            k_number += 1
print(k_number)

