
g = int(input().strip())
for a0 in range(g):
    n = int(input().strip())
    sequence = list(map(int, input().strip().split(' ')))

    moves = 1
    is_moves = True
    while is_moves:
        dels = 0
        for i in range(1, len(sequence) - 1):
            if len(sequence) == 2:
                is_moves = False
                if moves % 2 == 0:
                    print('Alice')
                else:
                    print('Bob')
            if i >= len(sequence):
                continue
            if sequence[i - 1] == 0 and sequence[i + 1] == 0:
                del sequence[i]
                dels += 1
                moves += 1
        if dels == 0:
            is_moves = False
    if moves % 2 == 0:
        print('Alice')
    else:
        print('Bob')




