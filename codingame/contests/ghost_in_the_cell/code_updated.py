"""
https://www.codingame.com/ide/challenge/ghost-in-the-cell
"""

import sys
import math


class IndirectedWeightedGraph:
    def __init__(self):
        self.__adjacent = {}
        self.__weights = {}

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

        if destination in self.__adjacent:
            self.__adjacent[destination].append(source)
        else:
            self.__adjacent[destination] = [source]

    def adjacent_nodes(self, source):
        return set(self.__adjacent[source])

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
        # player that owns the troop: 1 for you or -1 for your opponent
        self.arg_1 = arg_1_

        # number of cyborgs in the factory
        # identifier of the factory from where the troop leaves
        # identifier of the factory from where the bomb launched
        self.arg_2 = arg_2_

        # factory production (between 0 and 3)
        # identifier of the factory targeted by the troop
        # identifier of the factory targeted by the bomb if yours, -1 otherwise
        self.arg_3 = arg_3_

        # unused
        # number of cyborgs in the troop (positive integer)
        # remaining amount of turn before explosion, -1 otherwise
        self.arg_4 = arg_4_

        # unused
        # remaining number of turns before the troop arrives (positive integer)
        # unused
        self.arg_5 = arg_5_


class GameData:
    def __init__(self):
        self.units = []

    def add_unit(self, unit):
        self.units.append(unit)

    def get_units(self):
        return self.units


class Heuristics:

    # @ tuning params
    score_params = {
        'production': 100,
        'distance': -0.5,
        'defence': -1,
        'enemy_outpost': 1,
    }
    MAX_RANGE_FACTORY = 20

    # states
    states = ['WAIT', 'EXPANSE', 'DEFENSE', 'DOMINATE', 'UNDER_BOMB']
    initial_state = 'WAIT'
    current_state = None

    def __init__(self, game_data_units):
        self.game_units = game_data_units
        self.print_command = ''

    def __get_all_production(self):
        other_production, my_production = 0, 0
        for factory in self.game_units:
            if factory.type_ == 'FACTORY':
                if factory.arg_1 == 1:
                    my_production += factory.arg_3
                else:
                    other_production += factory.arg_3
        return my_production, other_production

    def __get_all_troops(self):
        other_cyborgs, my_cyborgs = 0, 0
        for factory in self.game_units:
            if factory.arg_1 == 1:
                my_cyborgs += factory.arg_3
            else:
                other_cyborgs += factory.arg_3
        return my_cyborgs, other_cyborgs

    def __get_neutral_factory(self):
        neutral = 0
        for factory in self.game_units:
            if factory.type_ == 'FACTORY':
                if factory.arg_1 == 0:
                    neutral += 1
        return neutral

    def __get_my_factories(self):
        my_factories = []
        for factory in self.game_units:
            if factory.type_ == 'FACTORY' and factory.arg_1 == 1:
                my_factories.append(factory)
        return my_factories

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

    def __attacked_by_bomb(self):
        for unit in self.game_units:
            if unit.id_ == 'BOMB' and unit.arg_1 == -1:
                return True
        return False

    def update(self):
        self.current_state = self.initial_state

        # can I win by production and amount?
        my_production, other_production = self.__get_all_production()
        my_troops, other_troops = self.__get_all_troops()
        neutral_factory = self.__get_neutral_factory()
        if (my_production > other_production) and (my_troops > other_troops) and (neutral_factory == 0):
            self.current_state = 'DOMINATE'
            print('LOG: Activate state: %s' % self.current_state, file=sys.stderr)
            return self.current_state

        # if I have been attacked by BOMB?
        if self.__attacked_by_bomb():
            self.current_state = 'UNDER_BOMB'
            print('LOG: Activate state: %s' % self.current_state, file=sys.stderr)
            return self.current_state

        # if I have been attacked?
        if self.__calculate_under_attack_factories() > 0:
            self.current_state = 'DEFENSE'
            print('LOG: Activate state: %s' % self.current_state, file=sys.stderr)
            return self.current_state

        # Expanse
        self.current_state = 'EXPANSE'
        print('LOG: Activate state: %s' % self.current_state, file=sys.stderr)
        return self.current_state

    # state DOMINATE active
    def _state_dominate_active(self):
        pass

    # state UNDER_BOMB active
    def _state_under_bomb_active(self):
        pass

    # state DEFENSE active
    def _state_defense_active(self):
        pass

    # state EXPANSION active
    def __get_best_home_factory(self):
        my_factories = self.__get_my_factories()
        best_factory = my_factories[0]
        for candidate in my_factories:
            if best_factory.arg_2 < candidate.arg_2:
                best_factory = candidate
        return best_factory

    @staticmethod
    def __get_the_best_key(dict_):
        v = list(dict_.values())
        k = list(dict_.keys())
        return k[v.index(max(v))]

    def __get_the_target_factory(self, current_home):
        unit_balancer = {}
        for unit in self.game_units:
            if (unit.id_ == current_home.id_) or (unit.type_ == 'TROOP') or (unit.arg_1 == 1):
                continue

            if weighted_graph.get_weight(current_home.id_, unit.id_) <= self.MAX_RANGE_FACTORY:
                unit_balancer[unit] = unit.arg_2 * self.score_params['defence']
                unit_balancer[unit] += unit.arg_3 * self.score_params['production']
                unit_balancer[unit] += weighted_graph.get_weight(current_home.id_, unit.id_) * self.score_params['distance']

        if len(unit_balancer) == 0:
            return 0
        return self.__get_the_best_key(unit_balancer)

    def __get_another_target_factory(self, current_home, used_factories):
        unit_balancer = {}
        for unit in self.game_units:
            if (unit.id_ == current_home.id_) or (unit.type_ == 'TROOP') or (unit.arg_1 == 1):
                continue

            if unit in used_factories:
                continue

            if weighted_graph.get_weight(current_home.id_, unit.id_) <= self.MAX_RANGE_FACTORY:
                unit_balancer[unit] = unit.arg_2 * self.score_params['defence']
                unit_balancer[unit] += unit.arg_3 * self.score_params['production']
                unit_balancer[unit] += weighted_graph.get_weight(current_home.id_, unit.id_) * self.score_params['distance']

        if len(unit_balancer) == 0:
            return 0
        return self.__get_the_best_key(unit_balancer)

    @staticmethod
    def __if_capture_possible(home, target, troops):
        capture_amount = 10000
        if target.arg_1 == -1:
            capture_amount = target.arg_2 + target.arg_3 * weighted_graph.get_weight(home.id_, target.id_) + 1 - troops
        elif target.arg_1 == 0:
            capture_amount = target.arg_2 + 1 - troops
        if capture_amount <= home.arg_2:
            return True, capture_amount
        return False

    def __if_troops_already_sent(self, home, target):
        deficit = [False, 0]
        for unit in self.game_units:
            if unit.type_ == 'TROOP' and unit.arg_1 == 1:
                if unit.arg_2 == home.id_ and unit.arg_3 == target.id_:
                    deficit[0] = True
                    deficit[1] += unit.arg_4
        return deficit

    def _state_expanse_active(self):
        # TODO add this for all factories
        home_factory = self.__get_best_home_factory()
        best_target = self.__get_the_target_factory(home_factory)
        if best_target != 0:
            # if troops have already sent to attack this factory
            troops_on_the_way = self.__if_troops_already_sent(home_factory, best_target)

            if self.__if_capture_possible(home_factory, best_target, troops_on_the_way[1])[0]:
                capture_amount = self.__if_capture_possible(home_factory, best_target, troops_on_the_way[1])[1]
                command = 'Move %s %s %s' % (home_factory.id_, best_target.id_, capture_amount)
                self._add_command(command)
            else:
                # can I make a donation to factory?
                if home_factory.arg_2 > 10 and home_factory.arg_3 < 3:
                    command = 'INC %s' % home_factory.id_
                    self._add_command(command)

        # add activity for the other my factories:
        my_factories = self.__get_my_factories()
        my_factories.remove(home_factory)
        list_of_best_targets = [best_target]
        if my_factories:
            for next_factory in my_factories:
                best_target = self.__get_another_target_factory(next_factory, list_of_best_targets)
                if best_target != 0:
                    # if troops have already sent to attack this factory
                    troops_on_the_way = self.__if_troops_already_sent(next_factory, best_target)

                    if self.__if_capture_possible(next_factory, best_target, troops_on_the_way[1])[0]:
                        capture_amount = self.__if_capture_possible(next_factory, best_target, troops_on_the_way[1])[1]
                        command = 'Move %s %s %s' % (next_factory.id_, best_target.id_, capture_amount)
                        self._add_command(command)
                    else:
                        # can I make a donation to factory?
                        if next_factory.arg_2 > 10 and next_factory.arg_3 < 3:
                            command = 'INC %s' % next_factory.id_
                            self._add_command(command)
                    list_of_best_targets.append(best_target)

    def run(self):
        if self.current_state == 'WAIT':
            self.print_command = ''
            return self.print_command
        if self.current_state == 'DOMINATE':
            self._state_dominate_active()
        if self.current_state == 'UNDER_BOMB':
            self._state_under_bomb_active()
        if self.current_state == 'DEFENSE':
            self._state_defense_active()
        if self.current_state == 'EXPANSE':
            self._state_expanse_active()
        return self.print_command

    def _add_command(self, command):
        if self.print_command == 0:
            self.print_command = command
        if len(self.print_command) > 3:
            self.print_command += ';'
            self.print_command += command


factory_count = int(input())
link_count = int(input())
# print("Factory count = %s" % factory_count, file=sys.stderr)
# print("Link count = %s" % link_count, file=sys.stderr)

weighted_graph = IndirectedWeightedGraph()
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    weighted_graph.add_connection(factory_1, factory_2, distance)

# game loop
global_home_factory = None
while True:
    # initial
    game_data = GameData()

    entity_count = int(input())
    for _ in range(entity_count):
        entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5 = input().split()
        game_data.add_unit(Entity(int(entity_id),
                                  entity_type,
                                  int(arg_1), int(arg_2), int(arg_3), int(arg_4), int(arg_5)))

    bot = Heuristics(game_data.units)
    bot.update()
    result_command = bot.run()

    if result_command[len(result_command) - 1] == ';':
        result_command = result_command[:len(result_command) - 1]

    if result_command == '':
        print('Wait')
    else:
        print(result_command)
