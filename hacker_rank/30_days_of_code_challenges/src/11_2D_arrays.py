"""
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

"""

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

max_sum = -10000000000000

for row in range(0, 4):
    for column in range(0, 4):
        sum_glass = arr[0 + row][0 + column] + arr[0 + row][1 + column] + arr[0 + row][2 + column] \
                    + arr[1 + row][1 + column] + \
                    arr[2 + row][0 + column] + arr[2 + row][1 + column] + arr[2 + row][2 + column]


        if max_sum < sum_glass:
            max_sum = sum_glass

print(max_sum)
