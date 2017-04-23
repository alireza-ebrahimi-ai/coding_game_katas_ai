def solver(seq_, k_):
    if '-' not in seq_:
        return 0

    steps = 0
    seq_arr = list(seq_)
    for index in range(0, len(seq_)):
        if seq_arr[index] == '+':
            continue

        # change first - to +
        if index + k_ > len(seq_arr):
            if '-' in seq_arr:
                return 'IMPOSSIBLE'

        steps += 1
        for pos in range(index, index + k_):
            if seq_arr[pos] == '-':
                seq_arr[pos] = '+'
            else:
                seq_arr[pos] = '-'
    return steps


t = int(input())
for case in range(1, t + 1):
    seq, k = input().split()
    print('Case #%s: %s' % (case, solver(seq, int(k))))

