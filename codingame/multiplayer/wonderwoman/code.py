import time
import sys


class Board:
    def __init__(self, s):
        self.size = s
        self.initial_position = []

    def add_row(self, r):
        self.initial_position.append(r)


class Player:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]


GAME_BOARD = Board(int(input()))
UNITS_PER_PLAYER = int(input())
MY_UNITS = []
ENEMY_UNITS = []
VALID_COMMANDS = []

while True:
    for i in range(GAME_BOARD.size):
        GAME_BOARD.add_row(input())
    for k in range(UNITS_PER_PLAYER):
        MY_UNITS.append(Player([int(j) for j in input().split()]))
    for m in range(UNITS_PER_PLAYER):
        ENEMY_UNITS.append(Player([int(j) for j in input().split()]))
    legal_actions = int(input())
    for n in range(legal_actions):
        command, idx, direction_1, direction_2 = input().split()
        VALID_COMMANDS.append([command, direction_1, direction_2])

    print('My unit: %s' % MY_UNITS[0].x, file=sys.stderr)
    print("MOVE&BUILD 0 N S")


