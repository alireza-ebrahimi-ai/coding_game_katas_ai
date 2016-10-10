"""
Codingame challenge: The Accountant

"""

import sys
import math

"""
The order in which actions happens in between two rounds is:
   Enemies move towards their targets.
   If a MOVE command was given, Wolff moves towards his target.
   Game over if an enemy is close enough to Wolff.
   If a SHOOT command was given, Wolff shoots an enemy.
   Enemies with zero life points are removed from play.
   Enemies collect data points they share coordinates with.

   MOVE x y or SHOOT id
   step not more than 1000 units
   less than 2000 units to enemy causes death
   enemy moves 500 units, if data close than 500 - its lost

Expert rules:
    When shooting an enemy, the damage dealt is 125 000 divided by x ** 1.2,
    rounded to the nearest integer; x is equal to the Euclidean distance between Wolff and the enemy.
    If several data points tie as the closest to an enemy, that enemy will aim for the data point with the smallest id.
"""


class GameMechanicsHelper:

    def update_globals(self, data_count, data_points, enemies, player, enemy_count):
        self.global_data_count = data_count
        self.global_data_points = data_points
        self.global_enemies = enemies
        self.global_player = player
        self.global_enemy_count = enemy_count

    @staticmethod
    def distance_to_object(object_1, object_2):
        return round(math.sqrt((object_1['x'] - object_2['x']) ** 2 + (object_1['y'] - object_2['y']) ** 2))

    def damage_dealt(self, player_, enemy):
        return round(125000 / self.distance_to_object(player_, enemy) ** 1.2)

    def return_new_pos(self, step, current_pos, target):
        max_dist = self.distance_to_object(current_pos, target)
        delta_dist = step / max_dist
        dx = target['x'] - current_pos['x']
        dy = target['y'] - current_pos['y']
        return round(current_pos['x'] + dx * delta_dist), round(current_pos['y'] + dy * delta_dist)

    def enemy_next_position(self, enemy, _data_points=None, _data_count=None):
        # check
        if _data_count is None:
            _data_count = self.global_data_count
        if _data_points is None:
            _data_points = self.global_data_points
        # find the nearest data
        the_nearest = 0
        for i in range(_data_count):
            if self.distance_to_object(enemy, _data_points[i]) < self.distance_to_object(enemy,
                                                                                         _data_points[the_nearest]):
                the_nearest = i
        return self.return_new_pos(500, enemy, _data_points[the_nearest])

    def player_next_position(self, target, player=None):
        if player is None:
            player = self.global_player
        return self.return_new_pos(1000, player, target)

    def move_to_objects_center(self, enemy_count=None, data_count=None, data_points=None, enemies=None, player=None):
        if enemy_count is None:
            enemy_count = self.global_enemy_count
        if data_count is None:
            data_count = self.global_data_count
        if data_points is None:
            data_points = self.global_data_points
        if enemies is None:
            enemies = self.global_enemies
        if player is None:
            player = self.global_player

        if enemy_count > 1:
            all_targets = data_count + enemy_count + 1
            all_x, all_y = 0, 0
            for data_id_ in range(data_count):
                all_x += data_points[data_id_]['x']
                all_y += data_points[data_id_]['y']
            for enemy_id_ in range(enemy_count):
                all_x += enemies[enemy_id_]['x']
                all_y += enemies[enemy_id_]['y']
            all_x += player['x']
            all_y += player['y']
            return round(all_x / all_targets), round(all_y / all_targets)
        else:
            the_nearest_data = 0
            for i in range(data_count):
                if self.distance_to_object(enemies[0], data_points[i]) < self.distance_to_object(
                                                                            enemies[0], data_points[the_nearest_data]):
                    the_nearest_data = i
            return data_points[the_nearest_data]['x'], data_points[the_nearest_data]['y']

    def find_the_closest_enemy_to_datapoint(self, data_count=None, enemy_count=None, data_points=None, enemies=None):
        if enemy_count is None:
            enemy_count = self.global_enemy_count
        if data_count is None:
            data_count = self.global_data_count
        if data_points is None:
            data_points = self.global_data_points
        if enemies is None:
            enemies = self.global_enemies
        answer = {'distance': 25000, 'enemy_num': 0, 'dp_num': 0}
        for id_dp in range(data_count):
            for id_enemy in range(enemy_count):
                distance = self.distance_to_object(data_points[id_dp], enemies[id_enemy])
                if distance < answer['distance']:
                    answer['distance'] = distance
                    answer['enemy_num'] = id_enemy
                    answer['dp_num'] = id_dp
        return answer

    def find_the_closest_enemy_to_player(self, enemy_count=None, player=None, enemies=None):
        if enemy_count is None:
            enemy_count = self.global_enemy_count
        if enemies is None:
            enemies = self.global_enemies
        if player is None:
            player = self.global_player

        answer = {'distance': 25000, 'enemy_num': 0}
        for id_enemy in range(enemy_count):
            distance = self.distance_to_object(player, enemies[id_enemy])
            if distance < answer['distance']:
                answer['distance'] = distance
                answer['enemy_num'] = id_enemy
        return answer


class GameOptimizer:
    global global_data_count, global_data_points, global_enemies, global_player, global_enemy_count

    def __init__(self):
        self.shots_current = 0
        self.hp_total = 0
        self.enemies_killed = 0
        self.enemies_begin = 0

    def extra_points(self):
        """
        DP * max(0, (L - 3 * S)) * 3, where:
            DP is the number of data points left.
            L is the total amount of life points enemies have among themselves at the start of the game.
            S is the total number of shots fired during play.
        """
        return global_data_count * max(0, (self.hp_total - 3 * self.shots_current)) * 3

    def count_score(self):
        if global_data_count > 0:
            score = global_data_count * 100 + self.enemies_killed * 10
            return score
        else:
            return 0

    def main_optimizer_v1(self):
        next_enemy_step = global_enemies[0]
        next_enemy_step['x'], next_enemy_step['y'] = game_mechanics.enemy_next_position(global_enemies[0])
        distance_to_target = game_mechanics.distance_to_object(global_enemies[0], global_data_points[0])
        max_depth = int(distance_to_target // 500)

        # generate all simple variations
        moves_tree = []
        for i in range(max_depth):
            temp = []
            for k in range(max_depth):
                if k < i:
                    temp.append(0)
                else:
                    temp.append(1)
            moves_tree.append(temp)

        # analisys the best solution
        best_analisys = {'score': 0, 'tree': ''}
        for decision in moves_tree:
            shoots = self.shots_current
            current_enemy_hp = global_enemies[0]['hp']
            player_predict = global_player
            enemy_predict = global_enemies[0]
            fail = False
            for move in decision:
                if move == 0:
                    # move x, y
                    if game_mechanics.distance_to_object(player_predict, enemy_predict) < 2000:
                        fail = True
                    player_predict['x'], player_predict['y'] = game_mechanics.return_new_pos(1000, player_predict,
                                                                                             global_data_points[0])
                    enemy_predict['x'], enemy_predict['y'] = game_mechanics.enemy_next_position(enemy_predict)
                else:
                    # shoot id
                    shoots += 1
                    current_enemy_hp -= game_mechanics.damage_dealt(player_predict, enemy_predict)
                    if current_enemy_hp <= 0:
                        score_move = 100 + 10 + 1 * max(0, (self.hp_total - 3 * shoots)) * 3
                        if (score_move > best_analisys['score']) and not fail:
                            best_analisys['score'] = score_move
                            best_analisys['tree'] = decision

        # debugging values & parameters:
        # print('Current score: %s' % current_score, file=sys.stderr)
        # print('HP_total: %s' % self.hp_total, file=sys.stderr)
        # print('Damage: %s' % current_damage, file=sys.stderr)
        # print('Next x,y of enemy: %s %s' % (next_enemy_step['x'], next_enemy_step['y']), file=sys.stderr)
        # print('Distance to target: %s' % distance_to_target, file=sys.stderr)
        # print('Moves to target: %s' % max_depth, file=sys.stderr)
        print(best_analisys, file=sys.stderr)

        return best_analisys['tree'][0]

    def main_optimizer_v2(self):
        # save all global parameters for simulating
        simulated_data_points = global_data_points
        simulated_enemy_count = global_enemy_count
        simulated_player = global_player
        simulated_data_count = global_data_count
        simulated_enemies = global_enemies

        # find the closest enemy to player and data_point
        the_closest_enemy_to_datapoint = game_mechanics.find_the_closest_enemy_to_datapoint()
        the_closest_enemy_to_player = game_mechanics.find_the_closest_enemy_to_player()
        distance_to_target_player = game_mechanics.distance_to_object(the_closest_enemy_to_player, simulated_player)
        max_depth_player = int(distance_to_target_player // 500)
        # distance_to_target_datapoint = game_mechanics.distance_to_object(the_closest_enemy_to_datapoint,
        # simulated_player)
        # max_depth_player = int(distance_to_target_player // 500)

        # generate all simple variations for closest enemy to player
        moves_tree_player = []
        for i in range(max_depth_player):
            temp = []
            for k in range(max_depth_player):
                if k < i:
                    temp.append(0)
                else:
                    temp.append(1)
            moves_tree_player.append(temp)

        # analisys the best solution
        best_analisys = {'score': 0, 'tree': ''}
        for decision in moves_tree_player:
            shoots = self.shots_current

            fail = False
            for move in decision:
                the_closest_enemy_to_player = game_mechanics.find_the_closest_enemy_to_player()
                if move == 0:
                    # move x, y
                    for id_sim in range(simulated_enemy_count):
                        if game_mechanics.distance_to_object(simulated_player, simulated_enemies[id_sim]) < 2000:
                            fail = True
                    new_target = {'x': 0, 'y': 0}
                    new_target['x'], new_target['y'] = game_mechanics.move_to_objects_center(simulated_enemy_count,
                                                                                             simulated_data_count,
                                                                                             simulated_data_points,
                                                                                             simulated_enemies,
                                                                                             simulated_player)

                    simulated_player['x'], simulated_player['y'] = game_mechanics.return_new_pos(
                        1000, simulated_player, new_target)

                    for id_sim in range(simulated_enemy_count):
                        simulated_enemies[id_sim]['x'], simulated_enemies[id_sim]['y'] = \
                            game_mechanics.enemy_next_position(simulated_enemies[id_sim],
                                                               simulated_data_points, simulated_data_count)
                else:
                    # shoot id
                    shoots += 1
                    the_closest_enemy_to_player['hp'] -= game_mechanics.damage_dealt(simulated_player, the_closest_enemy_to_player)
                    if the_closest_enemy_to_player['hp'] <= 0:
                        score_move = 100 + 10 + 1 * max(0, (self.hp_total - 3 * shoots)) * 3
                        if (score_move > best_analisys['score']) and not fail:
                            best_analisys['score'] = score_move
                            best_analisys['tree'] = decision

        print(best_analisys, file=sys.stderr)
        if best_analisys['tree'][0] == 0
        return best_analisys['tree'][0]

game_mechanics = GameMechanicsHelper()
optimizer = GameOptimizer()

first_round = True

while True:
    global_data_points = []
    global_enemies = []

    x, y = [int(i) for i in input().split()]  # x.max() = 16000, y.max() = 9000
    global_player = {'x': x, 'y': y}

    global_data_count = int(input())
    for i in range(global_data_count):
        data_id, data_x, data_y = [int(j) for j in input().split()]
        global_data_points.append({'id': data_id, 'x': data_x, 'y': data_y})

    global_enemy_count = int(input())
    for i in range(global_enemy_count):
        enemy_id, enemy_x, enemy_y, enemy_life = [int(j) for j in input().split()]
        global_enemies.append({'id': enemy_id, 'x': enemy_x, 'y': enemy_y, 'hp': enemy_life})
        if first_round:
            optimizer.enemies_begin = global_enemy_count
            optimizer.hp_total += enemy_life
        first_round = False
    game_mechanics.update_globals(global_data_count, global_data_points, global_enemies, global_player,
                                  global_enemy_count)

    result = optimizer.main_optimizer_v1()
    if result == 0:
        x_move_player, y_move_player = game_mechanics.move_to_objects_center()
        print('MOVE %s %s' % (x_move_player, y_move_player))
    else:
        shooting_enemy_id = global_enemies[0]['id']
        print('SHOOT %s' % shooting_enemy_id)
        optimizer.shots_current += 1

    # To debug: print("Debug messages...", file=sys.stderr)
