n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

counts = [0, 0, 0]

for i in range(0, n):
    if arr[i] > 0:
        counts[0] += 1
    elif arr[i] < 0:
        counts[1] += 1
    elif arr[i] == 0:
        counts[2] += 1

print(str(counts[0] / n))
print(str(counts[1] / n))
print(str(counts[2] / n))