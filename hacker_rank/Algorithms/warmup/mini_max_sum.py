a, b, c, d, e = input().strip().split(' ')
numbers = [int(a), int(b), int(c), int(d), int(e)]

# get min and max
min_value = numbers[0]
max_value = numbers[0]
for number in numbers:
    if min_value > number:
        min_value = number
    if max_value < number:
        max_value = number

numbers.remove(max_value)
min_sum = sum(numbers)
numbers.append(max_value)
numbers.remove(min_value)
max_sum = sum(numbers)
print('%s %s' % (min_sum, max_sum))



