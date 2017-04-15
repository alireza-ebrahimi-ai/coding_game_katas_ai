import sys

vowel_set = ['a', 'e', 'i', 'o', 'u', 'y']

w = list(input().strip())
printed = False
for pos in range(len(w) - 1):
    if w[pos] == w[pos + 1]:
        print('No')
        printed = True
        break
    if w[pos] in vowel_set and w[pos + 1] in vowel_set:
        print('No')
        printed = True
        break
if not printed:
    print('Yes')




