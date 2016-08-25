"""
https://www.hackerrank.com/challenges/lisa-workbook
5 3
4 2 6 1 10
25 10
1 29 94 15 87 100 20 55 100 45 82 80 100 100 3 53 100 2 100 100 100 100 100 100 1
11
67 50
1 24 1 2 3 1 1 75 1 100 100 19 53 100 63 100 22 70 3 100 100 26 100 100 6 49 100 100 71 14 100 32 98 92 100 44 100 100 100 36 84 46 100 100 100 100 34 100 87 62 55 97 100 100 100 85 100 100 100 76 100 2 97 100 82 100 2
40
"""

n, k = map(int, input().split())
T = [int(x) for x in input().split()]

page = 1
count = 0
chapter = 1
problems = 0
while chapter <= n:
    nextproblems = min((T[chapter - 1] - problems), k)
    if page > problems and page <= (problems + nextproblems):
        count += 1
    page += 1
    problems += nextproblems
    if problems == T[chapter - 1]:
        chapter += 1
        problems = 0

print(count)
