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

    def letter_size(self, letters):
        converted = []
        for letter in letters:
            converted.append(ord(letter) - 97)
        return converted

    def word_to_array(self, word):
        return list(word)

    def longest_suffix(self, word):
        the_longest_one = word[len(word) - 1]
        for position in range(len(word) - 2, -1, -1):
            if word[position:position + 1] >= the_longest_one[len(the_longest_one) - 1:]:
                the_longest_one = word[position:]
            else:
                return the_longest_one
        return the_longest_one

    def pivot(self, the_longest_suffix, word):
        if len(the_longest_suffix) == len(word):
            return 0
        return word[len(word) - len(the_longest_suffix) - 1:len(word) - len(the_longest_suffix)]

    def swap(self, pivot, longest_suffix):
        buffer = []
        if len(longest_suffix) == 1:
            return longest_suffix + pivot
        for i in range(len(longest_suffix) - 1, 0, -1):
            if pivot > longest_suffix[i]:
                buffer.append(pivot)
                pivot = longest_suffix[i]
                if i < len(longest_suffix):
                    if len(buffer) > 1:
                        buffer = list(reversed(buffer))
                    buffer.append(longest_suffix[:i])
                    buffer.append(pivot)
                return ''.join(list(reversed(buffer)))
            else:
                buffer.append(longest_suffix[i])
        return ''.join(list(reversed(buffer)))

    def reverse(self, suffix):
        return suffix[::-1]

    def collect_all(self, word, swap):
        if len(word) == len(swap):
            return swap
        else:
            return word[len(word) - len(swap)] + swap

    def merge_all(self, arr_num):
        arr_letter = []
        if arr_num:
            for index in arr_num:
                arr_letter.append(chr(index + 97))
            return ''.join(arr_letter)
        return 'no answer'

    def next_permutation(self, arr):
        i = len(arr) - 1
        while i > 0 and arr[i - 1] >= arr[i]:
            i -= 1
        if i <= 0:
            return False

        j = len(arr) - 1
        while arr[j] <= arr[i - 1]:
            j -= 1
        arr[i - 1], arr[j] = arr[j], arr[i - 1]

        arr[i:] = arr[len(arr) - 1: i - 1: -1]
        return arr

perm = Permutation()

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(input().strip())

for i in range(n):
    if len(arr[i]) > 1:
        raw_arr = perm.next_permutation(perm.letter_size(perm.word_to_array(arr[i])))
        answer = perm.merge_all(raw_arr)
        if answer == arr[i]:
            print('no answer')
        else:
            print(answer)
    else:
        print('no answer')