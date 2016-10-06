def nextMove(n, r, c, grid):
    coords_princess = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                coords_princess.append(i)
                coords_princess.append(j)

    if r < coords_princess[0]:
        if c < coords_princess[1]:
            return 'DOWN'
          # print('RIGHT')
        elif c > coords_princess[1]:
         #  print('DOWN')
            return 'LEFT'
        elif c == coords_princess[1]:
            return 'DOWN'
    elif r > coords_princess[0]:
        if c < coords_princess[1]:
            return 'UP'
        elif c > coords_princess[1]:
            return 'LEFT'
        elif c == coords_princess[1]:
            return 'UP'
    else:
        if c < coords_princess[1]:
            return 'RIGHT'
        else:
            return 'LEFT'


n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n, r, c, grid))
