"""
Server for generate games and tests

 1. open strategy
 2. generate start conditions
 3. simulate AI player
 4. return valid input to strategy

First line: 6 integers x & y for your pod's position. nextCheckpointX & nextCheckpointY for the coordinates
of the next checkpoint the pod must go through. nextCheckpointDist for the computed distance between your pod
and the next checkpoint, nextCheckpointAngle for the angle in degrees between your pod orientation and the direction
of the next checkpoint (from -180 to 180).

Second line: 2 integers opponentX & opponentY for the opponent pod's position.
"""

import math
from codingame.multiplayer.CSB.src.emulator import Checkpoint
from codingame.multiplayer.CSB.src.emulator import Pod
from codingame.multiplayer.CSB.src.emulator import Emulator

from codingame.multiplayer.CSB.src.code import game_loop


class Server:
    # map section
    MAP_SIZE = [16000, 9000]

    # checkpoint section
    CHECKPOINT_RADIUS = 600
    MIN_CHECKPOINT = 2
    MAX_CHECKPOINT = 4
    MIN_DISTANCE_TO_BORDER = 1000
    MAX_LAP = 1

    # pod section
    THRUST_MAX = 100
    POD_RADIUS = 400

    # current map
    checkpoint_amount = None
    checkpoints = []

    # game loop
    hero_pod = None
    enemy_pod = None
    strategy_answer = None

    def __init__(self):
        # TODO random generation
        self.checkpoint_amount = self.MAX_CHECKPOINT
        self.checkpoints.append(Checkpoint(3000, 3000))
        self.checkpoints.append(Checkpoint(6000, 3000))
        self.checkpoints.append(Checkpoint(6000, 6000))

        # TODO random generation
        self.hero_pod = Pod(initial_x=2800, initial_y=2800)
        self.enemy_pod = Pod(initial_x=3200, initial_y=3200)

        self.hero_pod.next_checkpoint_id = 1
        self.enemy_pod.next_checkpoint_id = 1

        # init emulator
        self.emulator = Emulator(self.hero_pod, self.enemy_pod, self.checkpoints)

    def receive_data_from_strategy(self, message):
        message = message.split(' ')
        strategy_x = message[1]
        strategy_y = message[2]
        thruster = -1

        if message[3] == 'BOOST':
            thruster = 'BOOST'
        elif message[3] == 'SHIELD':
            thruster = 'SHIELD'
        else:
            try:
                thruster = int(message[3])
            except ArithmeticError:
                print('Bad input')

        self.strategy_answer = [strategy_x, strategy_y, thruster]
        return self.strategy_answer

    def send_data_to_strategy(self, player):
        data = []
        if player == 'hero':
            data.append(self.hero_pod.x)
            data.append(self.hero_pod.y)
        elif player == 'enemy':
            data.append(self.enemy_pod.x)
            data.append(self.enemy_pod.y)

























