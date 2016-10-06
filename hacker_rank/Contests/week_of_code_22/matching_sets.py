"""
week of code 22, task 3

3
1 2 3
-1 4 3
= 2

3
1 2 3
2 3 2
= -1
"""

n = int(input().strip())
x = [int(a_temp) for a_temp in input().strip().split(' ')]
y = [int(a_temp) for a_temp in input().strip().split(' ')]

x = sorted(x)
y = sorted(y)
steps = 0


for i in range(n):
    if x[i] > y[i]:
        x[i] = x[i] - 1
        changed = False
        for j in range(i + 1, n):
            if x[j] < y[j]:
                x[j] = x[j] + 1
                changed = True
            if changed:
                steps += 1
                break
            else:
                x[i] = x[i] + 1

    elif x[i] < y[i]:
        x[i] = x[i] + 1
        changed = False
        for j in range(i, n):
            if x[j] > y[j]:
                x[j] = x[j] - 1
                changed = True
            if changed:
                steps += 1
                break
            else:
                x[i] = x[i] - 1

print(sorted(x))
print(sorted(y))
if sorted(x) == sorted(y):
    print(steps)
else:
    print(-1)









