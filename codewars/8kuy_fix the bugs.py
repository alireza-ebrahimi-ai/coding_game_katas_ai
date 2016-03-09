def my_first_kata(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return False
    else:
        return a % b + b % a