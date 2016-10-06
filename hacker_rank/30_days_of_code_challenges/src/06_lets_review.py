"""
Given a string, S of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2
space-separated strings on a single line (see the Sample below for more detail).
"""

N = int(input().strip())
list_of_strings = []

for i in range(0, N):
    strings = input().strip()
    list_of_strings.append(strings)

for i in range(0, N):
    answer = list_of_strings[i][::2] + ' ' + list_of_strings[i][1::2]
    print(answer)