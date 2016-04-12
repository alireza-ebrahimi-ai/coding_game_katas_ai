def calc(number):
    answer = 1
    for i in range(1, number + 1):
        answer = answer * i
    return answer

def sum_factorial(lst):
    answer = 0
    for i in range(0, len(lst)):
        answer = answer + calc(lst[i])

    return answer
