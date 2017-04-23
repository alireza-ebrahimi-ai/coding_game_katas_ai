n = int(input().strip())

delimeter_adds = 1
delimeter_current = 2
calculation = True
while calculation:
    if n % delimeter_current != 0:
        print(delimeter_current)
        break
    if delimeter_current > n:
        calculation = False
        print(delimeter_current)
        break
    delimeter_current += 1
