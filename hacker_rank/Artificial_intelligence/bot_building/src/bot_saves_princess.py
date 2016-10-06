"""
Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the
grid and can move one step at a time in any of the four directions. Can you rescue the princess?

3
---
-m-
p--
"""

def displayPathtoPrincess(n, grid):
    coords_bot = []
    coords_princess = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                coords_bot.append(i)
                coords_bot.append(j)
            if grid[i][j] == 'p':
                coords_princess.append(i)
                coords_princess.append(j)

    while coords_bot != coords_princess:
        if coords_bot[0] < coords_princess[0]:
            if coords_bot[1] < coords_princess[1]:
                print('DOWN')
                print('RIGHT')
                coords_bot[0] += 1
                coords_bot[1] += 1
            elif coords_bot[1] > coords_princess[1]:
                print('DOWN')
                print('LEFT')
                coords_bot[0] += 1
                coords_bot[1] -= 1
            elif coords_bot[1] == coords_princess[1]:
                print('DOWN')
                coords_bot[0] += 1
        elif coords_bot[0] > coords_princess[0]:
            if coords_bot[1] < coords_princess[1]:
                print('UP')
                print('RIGHT')
                coords_bot[0] -= 1
                coords_bot[1] += 1
            elif coords_bot[1] > coords_princess[1]:
                print('UP')
                print('LEFT')
                coords_bot[0] -= 1
                coords_bot[1] -= 1
            elif coords_bot[1] == coords_princess[1]:
                print('UP')
                coords_bot[0] -= 1
        else:
            if coords_bot[1] < coords_princess[1]:
                print('RIGHT')
                coords_bot[1] += 1
            else:
                print('LEFT')
                coords_bot[1] -= 1

m = int(input())
grid = []

for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
