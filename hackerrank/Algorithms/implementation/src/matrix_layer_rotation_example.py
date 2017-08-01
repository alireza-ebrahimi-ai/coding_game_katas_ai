# Based on hackrank's challenge:
# https://www.hackerrank.com/challenges/matrix-rotation-algo
# by rafael_augusto

from collections import deque
from itertools import chain

class Matrix():

    def __init__(self, m=None):
        self.m = m or list()

    def size(self):
        if len(self.m) == 0:
            return 0, 0

        return len(self.m), len(self.m[0])

    def _iter_rings_indexes(self):
        rows, cols = self.size()
        start = [0, 0]
        end = [rows - 1, cols - 1]

        while (end[0] - start[0] >= 1 and end[1] - start[1] >= 1) or start == end:

            def iter_ring():
                indexes = chain(
                    [(start[0], x) for x in range(start[1], end[1] + 1)],
                    [(x, end[1]) for x in range(start[0], end[0] + 1)],
                    [(end[0], x) for x in range(end[1], start[1] - 1, - 1)],
                    [(x, start[1]) for x in range(end[0], start[0] - 1, - 1)]
                )

                seen = set()

                # Elegantly avoids yielding the same item twice
                for x in indexes:
                    if x not in seen:
                        seen.add(x)
                        yield x

            yield iter_ring

            start = [x + 1 for x in start]
            end = [x - 1 for x in end]

    def rotate(self, n):
        for iter_ring in self._iter_rings_indexes():
            d = deque()

            for e in iter_ring():
                d.append(self.m[e[0]][e[1]])

            d.rotate(n)

            for e in iter_ring():
                self.m[e[0]][e[1]] = d.popleft()

        return self

    def __str__(self):
        return str(self.m)


def read_tuple():
    return [int(x) for x in input().split(' ')]


m, n, r = read_tuple()
matrix = Matrix([read_tuple() for i in range(0, m)])
matrix.rotate(-r)

for row in matrix.m:
    print(' '.join([str(x) for x in row]))