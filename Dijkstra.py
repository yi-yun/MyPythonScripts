nodes = ('A', 'B', 'C', 'D', 'E', 'F')
infinity = float("inf") #最大
graph = {
    'A': {'B': 10, 'D': 30, 'E': 45},
    'B': {'A': 10, 'C': 50, 'E': 40, 'F': 25},
    'C': {'B': 50, 'E': 35, 'F': 15},
    'D': {'A': 30, 'F': 20},
    'E': {'A': 45, 'B': 40, 'C': 35, 'F': 55},
    'F': {'B': 25, 'C': 15, 'D': 20, 'E': 55}
}
unvisited = {node: infinity for node in nodes}
visited = {}
current = 'A' # 假设是 A
currentDistance = 0
unvisited[current] = currentDistance
# print(unvisited)
while True:
    for neighbour, distance in graph[current].items():
        if neighbour not in unvisited:
            # print(neighbour,unvisited)
            continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited:
        break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

print(visited)
