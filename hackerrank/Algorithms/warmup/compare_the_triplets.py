"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges,
awarding points on a
scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

"""

a0, a1, a2 = input().strip().split(' ')
a = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b = [int(b0), int(b1), int(b2)]

score = [0, 0]
for i in range(0, 3):
    if a[i] < b[i]:
        score[1] += 1
    elif a[i] > b[i]:
        score[0] += 1
print(str(score[0]) + ' ' + str(score[1]))
