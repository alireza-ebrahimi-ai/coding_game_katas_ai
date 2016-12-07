import sys
import math


n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

ext_map = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ext_map[ext.lower()] = mt

print(ext_map, file=sys.stderr)

for _ in range(q):
    fname = input()
    print('test case: %s' % fname, file=sys.stderr)

    splitter = fname.split('.')
    if len(splitter) < 2:
        print('UNKNOWN')
    else:
        extension = splitter[len(splitter) - 1].lower()
        if extension in ext_map:
            print(ext_map[extension])
        else:
            print('UNKNOWN')



