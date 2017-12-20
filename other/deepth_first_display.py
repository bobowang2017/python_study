graph = [
    #   A  B  C  D  E
    ['', 'A', 'B', 'C', 'D', 'E'],
    ['A', -1, 5, -1, 5, 7],
    ['B', -1, -1, 4, -1, -1],
    ['C', -1, -1, -1, 8, 2],
    ['D', -1, -1, 8, -1, 6],
    ['E', -1, 3, -1, -1, -1]
]
vex = [0, 0, 0, 0, 0, 0]


def display(cur, sum, current_distance, route):
    if sum > current_distance:
        return
    if cur == len(vex) - 1:
        if sum < current_distance:
            current_distance = sum
            print('route: ' + route + '(distance =' + str(current_distance))+')'
        else:
            print('No distance')
        return

    for i in range(1, len(vex)):
        if graph[cur][i] > 0 and vex[i] == 0:
            vex[i] = 1
            display(i, sum + graph[cur][i], current_distance, route + '-->' + str(graph[0][i]))
            vex[i] = 0


if __name__ == '__main__':
    for i in range(1, len(vex)):
        display(i, 0, 99999, graph[0][i])
