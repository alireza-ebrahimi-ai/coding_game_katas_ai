"""
A polygon is a closed shape with three or more sides.
For example, triangles are polygons.
A polygon is non-degenerate if it has no overlapping sides (and no sides of zero length).

You have n sticks with positive integer lengths, a.
You want to create a polygon using all n sticks.
Because this is not always possible, you can cut one or more sticks into two smaller
sticks (they do not necessarily need to be of integer length) and repeat the
process of trying to create a polygon using all the sticks.
Given the lengths of all n sticks, find and print the minimum
number of cuts necessary to make a non-degenerate polygon.

3
3 4 5

= 0

"""

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

cuts = 0
if n == 1:
    print(2)
elif n == 2 and a[0] == a[1]:
    print(2)
else:
    for i in range(n):
        if a[i] >= sum(a) - a[i]:
            a[i] = a[i] / 2
            a.append((a[i]))
            cuts += 1
print(cuts)

