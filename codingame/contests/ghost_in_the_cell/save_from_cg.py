"""
https://www.codingame.com/ide/challenge/ghost-in-the-cell
"""

import sys
import math


class IndirectedWeightedGraph:
    def __init__(self):
        self.__adjacent = {}
        self.__weights = {}
        self.__vertex_count = 0
        self.__edges_count = 0

    def add_weight(self, vertex_1, vertex_2, weight):
        key_weight = '%s_%s' % (vertex_1, vertex_2)
        self.__weights[key_weight] = weight
        key_weight = '%s_%s' % (vertex_2, vertex_1)
        self.__weights[key_weight] = weight

    def get_weight(self, vertex_1, vertex_2):
        key_weight = '%s_%s' % (vertex_1, vertex_2)
        return self.__weights[key_weight]

    def add_connection(self, source, destination, weight):
        self.add_weight(source, destination, weight)

        if source in self.__adjacent:
            self.__adjacent[source].append(destination)
        else:
            self.__adjacent[source] = [destination]
            self.__vertex_count += 1

        if destination in self.__adjacent:
            self.__adjacent[destination].append(source)
        else:
            self.__adjacent[destination] = [source]
            self.__vertex_count += 1
        self.__edges_count += 1

    def adjacent_nodes(self, source):
        return set(self.__adjacent[source])

    def vertex_count(self):
        return self.__vertex_count

    def edges_count(self):
        return self.__edges_count

    def vertex_degree(self, source):
        if source in self.__adjacent:
            return len(self.__adjacent[source])
        else:
            return None

    def vertexes(self):
        return self.__adjacent.keys()


class Entity:
    def __init__(self, id_, type_, arg_1_, arg_2_, arg_3_, arg_4_, arg_5_):
        self.id_ = id_
        self.type_ = type_
        # player that owns the factory: 1 for you, -1 for your opponent and 0 if neutral
        # player that owns the troop: 1 for you or -1 for your opponent
        self.arg_1 = arg_1_

        # number of cyborgs in the factory
        # identifier of the factory from where the troop leaves
        self.arg_2 = arg_2_

        # factory production (between 0 and 3)
        # identifier of the factory targeted by the troop
        self.arg_3 = arg_3_

        # unused
        # number of cyborgs in the troop (positive integer)
        self.arg_4 = arg_4_

        # unused
        # remaining number of turns before the troop arrives (positive integer)
        self.arg_5 = arg_5_


class GameData:
    def __init__(self):
        self.units = []

    def add_unit(self, unit):
        self.units.append(unit)

    def get_units(self):
        return self.units


class MetaHeuristics:
    # @ tuning params
    score_params = {
        'production': 100,
        'distance': -0.5,
        'defence': -1,
        'enemy_outpost': 1,
    }
    MAX_RANGE_FACTORY = 20

    def __init__(self, game_data_units, start):
        self.game_units = game_data_units
        self.my_start_factory = start
        self.command = ''

    @staticmethod
    def __get_the_best_key(dict_):
        v = list(dict_.values())
        k = list(dict_.keys())
        return k[v.index(max(v))]

    def __get_the_best_factory(self):
        unit_balancer = {}
        for unit in self.game_units:
            if (unit.id_ == self.my_start_factory.id_) or (unit.type_ == 'TROOP') or (unit.arg_1 == 1):
                continue
            if unit.arg_3 < 1:
                continue

            if weighted_graph.get_weight(self.my_start_factory.id_, unit.id_) <= self.MAX_RANGE_FACTORY:
                unit_balancer[unit] = unit.arg_2 * self.score_params['defence']
                unit_balancer[unit] += unit.arg_3 * self.score_params['production']
                unit_balancer[unit] += weighted_graph.get_weight(self.my_start_factory.id_, unit.id_) * self.score_params['distance']

            # print("Score analisys for = %s, score %s" % (unit.id_, unit_balancer[unit.id_]), file=sys.stderr)

        # print("Best target with id = %s, the score is %s" % (self.__get_the_best_key(unit_balancer),
        #                                                      max(unit_balancer.values())), file=sys.stderr)
        if len(unit_balancer) == 0:
            return False
        # print('LOG: Unit Balancer length %s' % len(unit_balancer), file=sys.stderr)
        return self.__get_the_best_key(unit_balancer)

    def __check_my_troops_to_target(self, target, capture_amount):
        on_the_way = 0
        for unit in self.game_units:
            if (unit.type_ != 'TROOP') or (unit.arg_1 != 1):
                continue
            if unit.arg_3 == target.id_:
                on_the_way += unit.arg_4
        if on_the_way >= capture_amount:
            return True
        return False

    def __get_my_factories(self):
        my_factories = []
        for factory in self.game_units:
            if factory.type_ == 'FACTORY' and factory.arg_1 == 1:
                my_factories.append(factory)
        return my_factories

    def __get_all_production(self):
        other_production, my_production = 0, 0
        for factory in self.game_units:
            if factory.type_ == 'FACTORY':
                if factory.arg_1 == 1:
                    my_production += factory.arg_3
                else:
                    other_production += factory.arg_3
        return my_production, other_production

    def __calculate_under_attack_factories(self):
        my_factories = self.__get_my_factories()
        attacks = {}
        for factory in my_factories:
            for unit in self.game_units:
                if unit.id_ == 'TROOP' and unit.arg_1 == -1:
                    if unit.arg_3 == factory.id_:
                        if factory in attacks.keys():
                            attacks[factory] += unit.arg_4
                        else:
                            attacks[factory] = unit.arg_4
        return attacks

    def __get_supply_factory(self, under_attack):
        my_factories = self.__get_my_factories()
        best_supply = None
        for factory in my_factories:
            if factory in under_attack.keys():
                continue
            best_supply = factory
        if not best_supply:
            return False

        for factory in my_factories:
            if factory in under_attack.keys():
                continue
            if best_supply.arg_2 < factory.arg_2:
                best_supply = factory

        return best_supply

    def main_logic(self):
        command = ''
        command_sent = False

        # 1 Check if I have enough production to win
        # TODO - add killing blow
        my_production, other_production = self.__get_all_production()
        if my_production > other_production:
            print('LOG: Winning the game by production', file=sys.stderr)
            # 1.1 Activate defence mode
            print('LOG: Defence mode active', file=sys.stderr)
            under_attack = self.__calculate_under_attack_factories()
            if len(under_attack) == 0:
                print('Wait')
            else:
                # without priority
                for factory in under_attack.keys():
                    if under_attack[factory] < 1:
                        supply_factory = self.__get_supply_factory(under_attack)
                        if supply_factory:
                            # get the worst case
                            if min(under_attack.values()) < 1:
                                value = min(under_attack.values())
                                for factory_ in under_attack.keys():
                                    if under_attack[factory_] == value:
                                        command = 'Move %s %s %s' % (supply_factory.id_, factory_.id_, value)
                                        print(command)

                        else:
                            print('Wait')
                    else:
                        print('Wait')
        else:
            # 1. Set the active factory for capturing
            active_home_factory = self.my_start_factory

            # 2. Find the best target
            best_target = self.__get_the_best_factory()
            if not best_target:
                print('Wait')

            # 3. Check if I can capture it
            capture_amount = 25
            if best_target.arg_1 == -1:
                capture_amount = best_target.arg_2 + best_target.arg_3 * weighted_graph.get_weight(
                    active_home_factory.id_, best_target.id_) + 1
            elif best_target.arg_1 == 0:
                capture_amount = best_target.arg_2 + 1
            print('LOG: Capture id= %s, amount to send = %s' % (best_target.id_, capture_amount), file=sys.stderr)
            if capture_amount <= active_home_factory.arg_2:
                command = 'Move %s %s %s' % (active_home_factory.id_, best_target.id_, capture_amount)

            # 4. Check if I have enough cyborgs in the other factories
            my_factories = self.__get_my_factories()
            for potential_factory in my_factories:
                if potential_factory.arg_2 > capture_amount:
                    command = 'Move %s %s %s' % (potential_factory.id_, best_target.id_, capture_amount)

            print('LOG: Command %s' % command, file=sys.stderr)

            # 5. Check if I have already sent troops to capture
            if not self.__check_my_troops_to_target(best_target, capture_amount):
                print('LOG: Not enough to capture %s' % best_target.id_, file=sys.stderr)

                if command != '':
                    print(command)
                    command_sent = True

            if not command_sent:
                print('Wait')


factory_count = int(input())
link_count = int(input())
# print("Factory count = %s" % factory_count, file=sys.stderr)
# print("Link count = %s" % link_count, file=sys.stderr)

weighted_graph = IndirectedWeightedGraph()
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    weighted_graph.add_connection(factory_1, factory_2, distance)

# game loop
strategy_turn = 0
global_home_factory = None
while True:
    # initial
    strategy_turn += 1
    game_data = GameData()

    entity_count = int(input())
    for _ in range(entity_count):
        entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5 = input().split()
        game_data.add_unit(Entity(int(entity_id),
                                  entity_type,
                                  int(arg_1), int(arg_2), int(arg_3), int(arg_4), int(arg_5)))

        # print("Factory: id = %s type = %s, arg_1 = %s" % (entity_id, entity_type, arg_1), file=sys.stderr)
        if strategy_turn == 1:
            if (entity_type == 'FACTORY') and (int(arg_1) == 1):
                global_home_factory = Entity(int(entity_id), entity_type,
                                             int(arg_1), int(arg_2), int(arg_3), int(arg_4), int(arg_5))

    meta_heuristics = MetaHeuristics(game_data.units, global_home_factory)
    meta_heuristics.main_logic()
