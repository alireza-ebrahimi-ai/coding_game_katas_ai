import sys
import math


# constants
MAP = [16000, 7500]
my_team_id = int(input())  # if 0 you need to score on the right of the map, if 1 you need to score on the left


class Entities:
    entities_id = None
    entity_type = None  # "WIZARD", "OPPONENT_WIZARD" or "SNAFFLE" (or "BLUDGER" after first league)
    x = None
    y = None
    vx = None
    vy = None
    state = None        # 1 - wizard grabbed snaffle, 0 - otherwise

    def __init__(self, data):
        self.entities_id = data[0]
        self.entity_type = data[1]
        self.x = data[2]
        self.y = data[3]
        self.vx = data[4]
        self.vy = data[5]
        self.state = data[6]

# game loop
while True:
    game_entities = []
    entities = int(input())  # number of entities still in game
    for _ in range(entities):
        entity_id, entity_type, x, y, vx, vy, state = input().split()
        entitie = Entities([int(entity_id), entity_type, int(x), int(y), int(vx), int(vy), int(state)])
        game_entities.append(entitie)

    for i in range(2):
        # Edit this line to indicate the action for each wizard (0 ≤ thrust ≤ 150, 0 ≤ power ≤ 500)
        # i.e.: "MOVE x y thrust" or "THROW x y power"
        print("MOVE 8000 3750 100")
