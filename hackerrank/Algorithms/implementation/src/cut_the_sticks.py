"""
You are given N sticks, where the length of each stick is a positive integer.
A cut operation is performed on the sticks such that all of them are reduced by
the length of the smallest stick.
8
1 2 3 4 3 3 2 1
"""

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

iterator_ = 0

while len(arr) > 0:
    new_arr = []
    find_min = arr[0]
    iterator_ = 0
    for i in range(1, len(arr)):
        if find_min > arr[i]:
            find_min = arr[i]
    for i in range(0, len(arr)):
        if arr[i] - find_min >= 0:
            iterator_ += 1
            if arr[i] - find_min > 0:
                new_arr.append(arr[i] - find_min)
    print(iterator_)
    arr = new_arr




