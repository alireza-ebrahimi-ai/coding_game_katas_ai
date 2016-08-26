n = int(input().strip())
a = [int(A_temp) for A_temp in input().strip().split(' ')]

min = len(a)
empty = False
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            empty = True
            if min > abs(i - j):
                min = abs(i - j)
if empty:
    print(min)
else:
    print(-1)
