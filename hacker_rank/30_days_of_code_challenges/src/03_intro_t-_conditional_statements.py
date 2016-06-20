N = int(input().strip())

if N % 2 != 0:
    print("Weird")
elif N % 2 == 0 and (N > 2 and N < 6):
    print("Not Weird")
elif N % 2 == 0 and (N > 6 and N < 21):
    print("Weird")
elif N % 2 == 0 and N > 20:
    print("Not Weird")
