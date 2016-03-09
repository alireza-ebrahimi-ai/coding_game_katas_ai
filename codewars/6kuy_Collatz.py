def collatz(n):
    answer = str(n)
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        answer = answer + '->' + str(n)
    return answer



print collatz(4)
print collatz(3)