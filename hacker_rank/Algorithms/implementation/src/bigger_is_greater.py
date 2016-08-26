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


class Permutation:

    def word_size(self, word):
        return sum(map(lambda x: ord(x) - 96, word))

    def letter_size(self, letter):
        return ord(letter) - 96

    def longest_suffix(self, word):
        the_longest_one = word[len(word) - 1]
        for position in range(len(word) - 2, -1, -1):
            if word[position:position + 1] >= the_longest_one[len(the_longest_one) - 1:]:
                the_longest_one = word[position:]
        return the_longest_one

    def pivot(self, the_longest_suffix, word):
        if len(the_longest_suffix) == len(word):
            return 0
        return word[len(the_longest_suffix) - 1:len(the_longest_suffix)]
"""
perm = Permutation()

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(input().strip())


print(perm.longest_suffix('abcde'))
print(perm.longest_suffix('edcba'))
print(perm.longest_suffix('abcabc'))

print(perm.pivot(perm.longest_suffix('abcabc'), 'abcabc'))
"""