# from codingame.multiplayer.CSB.src.helpers import Constants
# from codingame.multiplayer.CSB.src.emulator import Emulator
#
# constants = Constants()
# emulator = Emulator()


def game_loop(server_data):

    x = server_data['x']
    y = server_data['y']
    next_checkpoint_x = server_data['next_checkpoint_x']
    next_checkpoint_y = server_data['next_checkpoint_y']
    next_checkpoint_dist = server_data['next_checkpoint_dist']
    next_checkpoint_angle = server_data['next_checkpoint_angle']
    opponent_x = server_data['opponent_x']
    opponent_y = server_data['opponent_y']

    thruster = 100
    if abs(next_checkpoint_angle) > 90:
        thruster = 0

    return '%s %s %s' % (next_checkpoint_x, next_checkpoint_y, thruster)
