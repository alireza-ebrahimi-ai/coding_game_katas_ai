def balance(arr1, arr2):
    dict_1, dict_2 = {}, {}

    for key in arr1:
        if key in dict_1:
            dict_1[key] += 1
        else:
            dict_1[key] = 1

    for key in arr2:
        if key in dict_2:
            dict_2[key] += 1
        else:
            dict_2[key] = 1

    if sorted(list(dict_1.values())) == sorted(list(dict_2.values())):
        return True
    return False


array1 = ["a", "a", "a", "a", "a", "b", "b", "b"]
array2 = ["c", "c", "c", "c", "c", "d", "d", "d"]

print(balance(array1, array2))
