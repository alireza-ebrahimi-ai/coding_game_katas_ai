"""
John Watson performs an operation called a right circular rotation on an array of integers
"""

n, k, q = input().strip().split(' ')
initial_data = [int(n), int(k), int(q)]
arr = [int(a_temp) for a_temp in input().strip().split(' ')]
q_arr = []
for _ in range(0, int(q)):
    q_arr.append(int(input().strip()))

for _ in range(0, int(k)):
    new_arr = []
    new_arr.append(arr[len(arr) - 1])
    for i in range(0, len(arr) - 1):
        new_arr.append(arr[i])
    arr = new_arr
for i in range(0, int(q)):
    print(arr[q_arr[i]])






