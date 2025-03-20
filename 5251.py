import sys
sys.stdin = open("input.txt", "r")

import heapq

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] * (N+1) for _ in range(N+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    #print(graph)

    INF = int(21e8)

    def dijkstra(start_node):
        pq = [(0, start_node)]
        dists = [INF] * (N+1)
        dists[start_node] = 0

        while pq:
            dist, node = heapq.heappop(pq)

            if dists[node] < dist:
                continue

            for next_info in graph[node]:
                next_dist = next_info[0]
                next_node = next_info[1]

                new_dist = dist + next_dist

                if dists[next_node] <= new_dist:
                    continue

                dists[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

        return dists

    result = dijkstra(0)
    print(f'#{tc} {result[-1]}')


