"""
Bob has a strange counter.
At the first second, t=1, it displays the number 3.
At each subsequent second, the number displayed by the counter decrements by 1.

"""

t = int(input().strip())

index = 1
answer = 3
multi = 3

while index != t:
    index += 1
    answer -= 1
    if answer == 0:
        multi = multi * 2
        answer = multi

print(answer)
if t < 4:
    print(4 - t)
else:
    n = 1
    pos = []
    while t > (3 * (2**n - 1)):
        pos.append(3 * (2**n - 1))
        n += 1
    range = 3 * (2**n - 1)
    print(range - pos[len(pos) - 1] - (t - pos[len(pos) - 1]) + 1)







