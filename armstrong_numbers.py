from itertools import combinations_with_replacement
A005188_list = []
for k in range(1, 12):
    a = [i**k for i in range(10)]
    for b in combinations_with_replacement(range(10), k):
        x = sum(map(lambda y:a[y], b))
        if x > 0 and tuple(int(d) for d in sorted(str(x))) == b:
            A005188_list.append(x)
A005188_list = sorted(A005188_list)
