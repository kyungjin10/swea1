import sys
sys.stdin = open("input.txt", "r")

def dfs(v, N):
    visited = [0] * (N + 1)
    stack = []
    path = []

    while True:
        if visited[v] == 0:
            visited[v] = 1
            path.append(str(v))

        for w in adj_list[v]:   # v에 인접하고 방문 안한 w가 있으면
            if visited[w] == 0:
                stack.append(v)
                v = w
                break
        else:       # 더이상 갈 곳이 없는 경우
            if stack:
                v = stack.pop()
            else:
                break

    print(f"#{tc} {'-'.join(path)}")

T = 1

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = list(map(int, input().split()))

    # 인접리스트 만들기
    adj_list = [[] for _ in range(V+1)]

    for i in range(E):
        v, w = graph[i*2], graph[i*2+1]

        adj_list[v].append(w)
        adj_list[w].append(v)

    # for i in range(1, V+1):
    #     adj_list[i].sort()

    dfs(1, V)