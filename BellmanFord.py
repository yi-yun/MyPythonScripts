nodes = ('A', 'B', 'C', 'D', 'E', 'F')
infinity = float("inf")  # 最大
graph = {
    'A': {'B': 10, 'D': 30, 'E': 45},
    'B': {'A': 10, 'C': 50, 'E': 40, 'F': 25},
    'C': {'B': 50, 'E': 35, 'F': 15},
    'D': {'A': 30, 'F': 20},
    'E': {'A': 45, 'B': 40, 'C': 35, 'F': 55},
    'F': {'B': 25, 'C': 15, 'D': 20, 'E': 55}
}


def bellman_ford(source):
    dist = {}
    p = {}
    for v in graph:
        dist[v] = infinity
        p[v] = None
    dist[source] = 0

    # print(dist,p)
    for i in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                # print(u,v)
                # 比较，要小的
                if dist[v] > graph[u][v] + dist[u]:
                    dist[v] = graph[u][v] + dist[u]
                    p[v] = u
                print(dist)


bellman_ford('B')
