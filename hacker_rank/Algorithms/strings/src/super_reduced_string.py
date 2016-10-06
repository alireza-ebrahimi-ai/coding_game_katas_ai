import re


task_string = input().strip()

letter = re.search('a', task_string)
print(letter.group())











