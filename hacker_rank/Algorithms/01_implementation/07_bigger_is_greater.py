"""
Given a word w, rearrange the letters of w to construct another word s in such a way that s
is lexicographically greater than w.
In case of multiple possible answers, find the lexicographically smallest one among them.

5
ab
bb
hefg
dhck
dkhc

=
ba
no answer
hegf
dhkc
hcdk
"""


def next_permutation(s):
  for i in reversed(range(len(s))):
    if s[i] > s[i-1]:
      break
  else:
    return []
  i -= 1
  for j in reversed(range(i + 1, len(s))):
    if s[j] > s[i]:
        break
  t = s[i]
  s[i] = s[j]
  s[j] = t
  s[i + 1:] = reversed(s[i + 1:])
  return s

t = int(input().strip())
w = []
for _ in range(t):
    w.append([arr_temp for arr_temp in input().strip().split(' ')])


print(next_permutation('ba'))
