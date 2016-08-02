"""
John Watson performs an operation called a right circular rotation on an array of integers
"""

n, k, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
k %= n
arr = arr[-k:] + arr[:-k]
for i in range(m):
    print(arr[int(input().strip())])






