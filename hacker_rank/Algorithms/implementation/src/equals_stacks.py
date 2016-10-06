"""
You have three stacks of cylinders where each cylinder has the same diameter,
but they may vary in height.
You can change the height of a stack by removing and discarding its topmost cylinder any number of times.
"""

from collections import deque

def read_queue():
    return deque(map(int, input().strip().split()))

nstacks = len(input().split())
stacks = [read_queue() for i in range(nstacks)]
heights = list(map(sum, stacks))

while len(set(heights)) > 1:
    ihighest = heights.index(max(heights))
    heights[ihighest] -= stacks[ihighest].popleft()

print(heights[0])



