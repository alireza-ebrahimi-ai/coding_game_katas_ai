"""
A Discrete Mathematics professor has a class of N students.
Frustrated with their lack of discipline, he decides to cancel class
if fewer than K students are present when class starts.

Given the arrival time of each student, determine if the class is canceled.

"""

t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    in_time = 0
    for j in range(0, n):
        if a[j] <= 0:
            in_time += 1
    if in_time >= k:
        print('NO')
    else:
        print('YES')


