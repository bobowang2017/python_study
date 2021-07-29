# -*- coding: utf-8 -*-
class Solution(object):
    def advantageCount(self, A, B):
        our_team = sorted(A)
        enemy_team = sorted([v, i] for i, v in enumerate(B))
        enemy_worst, enemy_best = 0, len(B) - 1
        for teammate in our_team:
            enemy, _ = enemy_team[enemy_worst]
            if teammate > enemy:                                # We are confident
                enemy_team[enemy_worst].append(teammate)        # Beat the enemy.
                enemy_worst += 1                                # Select the next worst enemy.
            else:                                               # We are not confident.
                enemy_team[enemy_best].append(teammate)         # Choose the enemy best.
                enemy_best -= 1                                 # Select the next best enemy.
        res = [t[2] for t in sorted(enemy_team, key=lambda x: x[1])]
        return res
