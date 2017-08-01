def solver(n_, k_):
    if n_ == k_:
        return 0, 0

    current_stalls = [1]
    for i in range(int(n_)):
        current_stalls.append(0)
    current_stalls.append(1)

    for person in range(1, int(k_) + 1):
        # calculate Ls Rs
        lr = []
        min_lr_max = 0
        max_lr_max = 0
        for pos in range(1, int(n_) + 1):

            if current_stalls[pos] == 1:
                lr.append([0, 0])
                continue
            l = 0
            for index in range(pos, 0, -1):
                if current_stalls[index - 1] == 1:
                    break
                l += 1
            r = 0
            for index in range(pos, int(n_)):
                if current_stalls[index + 1] == 1:
                    break
                r += 1
            lr.append([l, r])
            print(max(l, r), min(l, r))

            if min_lr_max < min(l, r):
                min_lr_max = min(l, r)
            if max_lr_max < max(l, r):
                max_lr_max = min(l, r)


        # choose place and fill current stalls
        for index_stalls in range(0, len(lr)):
            if min_lr_max == min(lr[index_stalls]):
                current_stalls[index_stalls + 1] = 1
                break
        print(current_stalls)
    return 0, 0


t = int(input())
for case in range(1, t + 1):
    n, k = input().split()
    if int(n) <= 10000000:
        max_, min_ = solver(n, k)
        print('Case #%s: %s %s' % (case, max_, min_))
