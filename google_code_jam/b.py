
def correct(ask):
    digits = list(str(ask))
    for pos in range(0, len(digits) - 1):
        if digits[pos] > digits[pos + 1]:
            return False
    return True


def solver(n_):
    max_int = int(n_)
    for answer in range(max_int, 0, -1):
        if correct(answer):
            return answer


def solver_large(n_):
    max_int = int(n_)
    if correct(max_int):
        return max_int
    digits = list(n_)
    level_dig = 0
    for pos in range(0, len(digits) - 1):
        if digits[pos] > digits[pos + 1]:
            level_dig = pos
            break

    if level_dig == 0:
        new_ans = []
        for pos in range(0, len(digits)):
            if pos == 0:
                if int(digits[0]) > 1:
                    new_ans.append(str(int(digits[pos]) - 1))
                else:
                    continue
            else:
                new_ans.append('9')
        return int(''.join(new_ans))

    else:
        ok = digits[:level_dig]
        if int(ok[len(ok) - 1]) - 1 > int(ok[len(ok) - 2]):
            new_ans = []
            for pos in range(0, len(digits)):
                if pos < level_dig - 1:
                    new_ans.append(digits[pos])
                if pos == level_dig - 1:
                    new_ans.append(str(int(digits[pos]) - 1))
                if pos >= level_dig:
                    new_ans.append('9')
            return int(''.join(new_ans))
        else:
            for i in range(len(ok) - 1, 0, -1):
                if int(ok[i - 1]) > int(ok[i]) - 1:
                    continue
                else:
                    new_level = i
                    new_ans = []
                    for pos in range(0, len(digits)):
                        if pos < new_level:
                            new_ans.append(digits[pos])
                        if pos == new_level:
                            new_ans.append(str(int(digits[pos]) - 1))
                        if pos > new_level:
                            new_ans.append('9')
                    return int(''.join(new_ans))
            # if switch to level - 1
            new_ans = []
            for pos in range(1, len(digits)):
                new_ans.append('9')
            return int(''.join(new_ans))


t = int(input())
for case in range(1, t + 1):
    n = input()
    if int(n) <= 1000000:
        print('Case #%s: %s' % (case, solver(n)))
    else:
        print('Case #%s: %s' % (case, solver_large(n)))
