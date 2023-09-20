# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

def make_graph(wires, n):

    connected_graph = [[] for i in range(n+1)]
    
    for i in range(len(wires)):
        connected_graph[wires[i][0]].append(wires[i][1])
        connected_graph[wires[i][1]].append(wires[i][0])
    
    return connected_graph

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    list_to_return = []

    while queue:
        starting = queue.popleft()
        list_to_return.append(starting)

        for item in graph[starting]:
            if visited[item] != True:
                queue.append(item)
                visited[item] = True
                
    return list_to_return

def solution(n, wires):
    answer = 100

    wires = sorted(wires, key = lambda x : (x[0], x[1]))

    
    for i in range(len(wires)):
        each_case = wires[:i] + wires[i+1:]

        connected = make_graph(each_case, n)
        
        length_of_graphs = set([])

        for j in range(1, n+1):
            visited = [False for k in range(n+1)]
            res = bfs(connected, j, visited)
            # print(res)
            length_of_graphs.add(len(res))

        if max(length_of_graphs) - min(length_of_graphs) < answer:
            answer = max(length_of_graphs) - min(length_of_graphs)
    # min = 100
    # for item in length_of_graphs:
    
    # print("--------------------")
    return answer
