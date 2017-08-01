"""
Given N names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for;
for each name queried, print the associated entry from your phone book
(in the form name=phoneNumber) or Not found  if there is no entry for .

"""

n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k, v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break



