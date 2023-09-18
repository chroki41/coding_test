from collections import deque

def solution(maps):
    answer = 0
    # for j in range(len(maps)):
    #     for i in range(len(maps[0])):
    #         maps = bfs(maps, (i, j), len(maps[0]), len(maps))
    maps = bfs(maps, (0, 0), len(maps[0]), len(maps))
    # for i in range(len(maps[0])):
    #     for j in range(len(maps)):
    #         maps = bfs(maps, (i, j), len(maps[0]), len(maps))

    if maps[-1][-1] == 1:
        return -1

    return maps[-1][-1]


def bfs(map, coordinate, maxx, maxy):
    queue = deque()
    queue.append(coordinate)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
    
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < maxx and ny <maxy and map[ny][nx] == 1 and map[coordinate[1]][coordinate[0]] != 0:
                map[ny][nx] = map[y][x] + 1
                queue.append((nx, ny))
                # print(map)
    return map
