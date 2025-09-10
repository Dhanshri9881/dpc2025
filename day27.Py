from collections import deque, defaultdict

def shortest_path(V, edges, start, end):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    if start == end:
        return 0

    visited = [False] * V
    distance = [-1] * V
    queue = deque([start])
    visited[start] = True
    distance[start] = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                if neighbor == end:
                    return distance[neighbor]
                queue.append(neighbor)
    return -1

print(shortest_path(5, [[0,1],[0,2],[1,3],[2,3],[3,4]], 0, 4))
print(shortest_path(3, [[0,1],[1,2]], 0, 2))
print(shortest_path(4, [[0,1],[1,2]], 2, 3))
