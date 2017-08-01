"""
https://www.hackerrank.com/challenges/find-digits
"""

t = int(input().strip())

for a0 in range(t):
    n = input().strip()
    n_div = int(n)
    answer = 0
    for digit in n:
        if int(digit) > 0:
            if n_div % int(digit) == 0:
                answer += 1
    print(answer)

