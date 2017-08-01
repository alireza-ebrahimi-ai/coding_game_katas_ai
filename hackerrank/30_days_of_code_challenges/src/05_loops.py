"""
Given an integer, , print its first  multiples.
Each multiple  (where ) should be printed on a new line in the form: N x i = result.
"""

N = int(input().strip())

for i in range(1, 11):
    print(str(N) + ' x ' + str(i) + ' = ' + str(N * i))
