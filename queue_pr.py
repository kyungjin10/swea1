from collections import deque

edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
graph = {}

for i in range(0, len(edges), 2):
    u, v = edges[i], edges[i+1]
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

#print(graph)
# for key in graph:
#     graph[key].sort()

def bfs(start):
    queue = deque([start])
    visited = set([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

bfs_result = bfs(1)

print("-".join(map(str, bfs_result)))

