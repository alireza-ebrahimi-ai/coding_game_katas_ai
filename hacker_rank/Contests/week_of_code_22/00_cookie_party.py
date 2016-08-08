"""
You're having a cookie party tonight!
You're expecting n guests and you've already made m cookies.
You want to distribute all the cookies evenly between your guests
in such a way that each guest receives the same number of whole cookies.
If there are not enough cookies to give everyone the same amount,
you must make some number of additional cookies.

Given n and m, find and print the minimum number of additional cookies
you must make so that everybody receives the same number of cookies.
"""

n, m = input().strip().split(' ')
guest, cookie = [int(n), int(m)]


if guest == cookie:
    print(0)
elif guest > cookie:
    print(guest - cookie)
else:
    multiply = 1
    while guest * multiply < cookie:
        multiply += 1
    print(guest * multiply - cookie)
