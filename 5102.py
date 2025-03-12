import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    graph = {}

    for i in range(E):
        S, G = arr[i][0], arr[i][1]
        if S not in graph:
            graph[S] = []
        if G not in graph:
            graph[G] = []

        graph[S].append(G)
        graph[G].append(S)

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
