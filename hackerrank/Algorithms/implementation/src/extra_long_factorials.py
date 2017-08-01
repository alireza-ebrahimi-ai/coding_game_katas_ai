n = int(input().strip())

if n == 1:
    print(1)
else:
    answer = 1
    for i in range(1, n):
        answer = answer * (i + 1)
    print(answer)