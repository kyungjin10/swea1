import sys
sys.stdin = open("input.txt", "r")

T = 1

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    graph = {}
    #print(edges)

    for i in range(0, len(edges), 2):
        V, E = edges[i], edges[i+1]
        if V not in graph:
            graph[V] = []
        if E not in graph:
            graph[E] = []

        graph[V].append(E)
        graph[E].append(V)

    for key in graph:
        graph[key].sort()


    def dfs(node, visited, result):
        visited.add(node)
        result.append(str(node))

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, result)


    visited = set()
    result = []

    dfs(1, visited, result)

    print(f'#{tc}', '-'.join(result))
