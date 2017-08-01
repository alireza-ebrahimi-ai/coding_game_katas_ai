
n = int(input().strip())
n_arr = list(map(int, input().strip().split()))


n_arr = sorted(n_arr)
amount = 0
index = 0
while index < n - 1:
    if (n_arr[index] == n_arr[index + 1]) or (n_arr[index] + 1 == n_arr[index + 1]):
        amount += 1
        index += 2
        if index + 1 == n:
            amount += 1
            break
    else:
        amount += 1
        index += 1
        if index + 1 == n:
            amount += 1
            break
if n < 2:
    print(1)
else:
    print(amount)



