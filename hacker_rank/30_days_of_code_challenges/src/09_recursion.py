"""
Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).

"""

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return n


n = int(input().strip())
print(factorial(n))
