
g = int(input().strip())
for a0 in range(g):
    n = int(input().strip())
    sequence = list(map(int, input().strip().split(' ')))

    moves = 0
    flag = True
    modify_arr = sequence[:]
    while flag:
        digits_taken = 0
        for i in range(1, len(modify_arr)):

            if len(modify_arr) - 1 <= i:
                continue

            if len(modify_arr) == 2:
                flag = False
                if moves % 2 == 0:
                    print('Bob')
                else:
                    print('Alice')

            if modify_arr[i - 1] == 0 and modify_arr[i + 1] == 0:
                del modify_arr[i]
                digits_taken += 1
                moves += 1
        if digits_taken == 0:
            flag = False

    if moves % 2 == 0:
        print('Bob')
    else:
        print('Alice')




