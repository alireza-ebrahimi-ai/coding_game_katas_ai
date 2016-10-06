
max_depth = 8

moves_tree = []
best_analisys = {'score': 0, 'tree': ''}
for i in range(max_depth):
    temp = []
    for k in range(max_depth):
        if k < i:
            temp.append(0)
        else:
            temp.append(1)
    moves_tree.append(temp)

print(moves_tree)

all_enemies_killed = False

# for decision in moves_tree:
#     while not all_enemies_killed:
#
#
#
#
#
#
#
#     for i in range(max_depth - pos):
#         tree_move.append(1)
#         shoots += 1
#         current_enemy_hp -= game_helper.damage_dealt(global_player, global_enemies[0])
#         if current_enemy_hp <= 0:
#             solution_not_find = False
#             score_move = 100 + 10 + 1 * max(0, (self.hp_total - 3 * shoots)) * 3
#             if score_move >= best_score:
#                 best_score = score
#                 best_tree = tree_move
#         break
