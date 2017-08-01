"""
https://www.hackerrank.com/challenges/utopian-tree
"""

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    tree_height = 1
    if n == 0:
        tree_height = 1
    elif n == 1:
        tree_height = 2
    else:
        if n % 2 == 0:
            for i in range(0, int(n / 2)):
                tree_height = tree_height * 2
                tree_height += 1
        else:
            for i in range(0, int((n - 1) / 2)):
                tree_height = tree_height * 2
                tree_height += 1
            tree_height = tree_height * 2
    print(tree_height)







