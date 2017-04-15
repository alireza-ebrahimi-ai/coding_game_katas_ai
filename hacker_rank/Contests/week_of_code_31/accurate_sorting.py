
q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))

    for i in range(1, len(a)):
        if (a[i - 1] > a[i]) and (a[i - 1] - a[i] == 1):
            a[i - 1], a[i] = a[i], a[i - 1]
    if a == sorted(a):
        print('Yes')
    else:
        print('No')



