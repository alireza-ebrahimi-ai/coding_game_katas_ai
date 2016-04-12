def unique_in_order(iterable):
    answer = []
    if iterable == "":
        return answer

    answer.append(iterable[0])
    position = 0
    index = 0
    while position < len(iterable):
        if answer[index] != iterable[position]:
            answer.append(iterable[position])
            index += 1
            position += 1
        else:
            position += 1
    return answer
