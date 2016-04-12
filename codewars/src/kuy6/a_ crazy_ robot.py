import math


def finaldist_crazyrobot(moves, init_pos):
    current_coords = []
    current_coords.append(init_pos[0])
    current_coords.append(init_pos[1])

    for step in range(0, len(moves)):
        if moves[step][0] == 'R':
           current_coords[0] += moves[step][1]
        if moves[step][0] == 'U':
           current_coords[1] += moves[step][1]
        if moves[step][0] == 'L':
          current_coords[0] -= moves[step][1]
        if moves[step][0] == 'D':
           current_coords[1] -= moves[step][1]

    return math.sqrt((init_pos[0]-current_coords[0]) ** 2 + (init_pos[1]-current_coords[1])**2)





init_pos = (0, 0)
moves = [('R', 2), ('U', 3), ('L', 1), ('D', 6)]

