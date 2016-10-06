"""
Given a set, S, of n distinct integers, print the size of a maximal subset, S',
of S where the sum of any 2 numbers in S' are not evenly divisible by k.
4 3
1 7 2 4

 = 3
"""

n, k = map(int, input().strip().split(" "))
numbers = map(int, input().strip().split(" "))

counts = [0] * k
for number in numbers:
    counts[number % k] += 1

count = min(counts[0], 1)
for i in range(1, k // 2 + 1):
    if i != k - i:
        count += max(counts[i], counts[k - i])
if k % 2 == 0:
    count += 1

print(count)




