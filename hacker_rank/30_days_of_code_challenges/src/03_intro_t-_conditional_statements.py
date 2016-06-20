N = int(input().strip())

if N % 2 != 0:
    print("Weird")
elif N % 2 == 0 and (N > 2 or N < 5):
    print("Not Weird")
elif N % 2 == 0 and (N > 6 or N < 20):
    print("Weird")
elif N % 2 == 0 and N > 20:
    print("Not Weird")
