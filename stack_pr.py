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

for key in graph:
    graph[key].sort()

#print(graph)

def dfs(node, visited, result):
    visited.add(node)
    result.append(str(node))

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, result)

visited = set()
result = []

dfs(1, visited, result)

print(' '.join(result))