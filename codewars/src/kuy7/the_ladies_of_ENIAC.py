import re

def rad_ladies(name):
    s_tuple = re.findall(r'[a-zA-Z! ]', name)
    answer =''
    for i in range(len(s_tuple)):
        answer = answer + s_tuple[i]

    return answer.upper()