# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from collections import deque

def solution(k, dungeons):
    n = 0    
    queue = deque()
    queue.append([k, []])

    all = []
    while queue:
        stamina, visited = queue.popleft()
        for item in dungeons:
            if item not in visited and stamina >= item[0]:
                # stamina = stamina - item[1]
                queue.append([stamina - item[1], visited + [item]])
                all.append(len(queue))
            else:
                n = max(n, len(visited))
    return n
