# -*- coding: utf-8 -*-
graph = [
    [0, 0, 0, 0, 0, 0],
    [0, -1, 2, -1, -1, 10],
    [0, -1, -1, 3, -1, 7],
    [0, 4, -1, -1, 4, -1],
    [0, -1, -1, -1, -1, 5],
    [0, -1, -1, -1, 3, -1],
]
vex = [0, 0, 0, 0, 0, 0]
min_val = 99999


def dfs(cur, distance, circuit):
    if distance > min_val:
        return
    if int(cur) + 1 == len(vex):
        print('distance=' + str(distance))
        print('circuit : ' + circuit)
        if distance < min_val:
            min_value = distance
        return

    for i in range(1, len(vex)):
        if graph[cur][i] > 0 and vex[i] == 0:
            vex[i] = 1
            dfs(i, distance + graph[cur][i], circuit+'-->'+str(i))
            vex[i] = 0


if __name__ == "__main__":
    vex[1] = 1
    dfs(1, 0, '1')
