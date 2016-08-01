"""
Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.


"""

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

new_arr = ''
for i in range(0, len(arr)):
    new_arr = new_arr + str(arr[len(arr) - i - 1]) + ' '

print(new_arr)