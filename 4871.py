import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    graph = {}

    for i in range(E):
        start, end = edges[i][0], edges[i][1]
        if start not in graph:
            graph[start] = []
        if end not in graph:
            graph[end] = []

        graph[start].append(end)

    start, target = edges[0][0], edges[-1][1]

    def dfs(node, visited):
        if node == target:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, visited):
                    return True
        return False


    # 출발점 또는 도착점이 그래프에 없으면 무조건 0 반환
    if start not in graph or target not in graph:
        dfs_result = 0
    else:
        # DFS 탐색을 실행하여 경로가 있는지 확인
        visited = set()  # 방문한 노드를 저장할 집합
        search_result = dfs(start, visited)  # DFS 실행

        # 경로가 존재하면 1, 존재하지 않으면 0
        if search_result:
            dfs_result = 1
        else:
            dfs_result = 0

    # 결과 출력
    print(f'#{tc} {dfs_result}')


