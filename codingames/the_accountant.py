import sys
import math

# Shoot enemies before they collect all the incriminating data!
# The closer you are to an enemy, the more damage you do but don't get too close or you'll get killed.


# game loop
while True:
    x, y = [int(i) for i in input().split()]
    data_count = int(input())
    for i in range(data_count):
        data_id, data_x, data_y = [int(j) for j in input().split()]
    enemy_count = int(input())
    for i in range(enemy_count):
        enemy_id, enemy_x, enemy_y, enemy_life = [int(j) for j in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # MOVE x y or SHOOT id
    print("MOVE 8000 4500")