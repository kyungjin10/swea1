import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    field = [list(map(str, input().strip())) for _ in range(N)]

    switch_cnt = 0
    min_cnt = 0

    def bfs(i, j):
        q = []
        visited = [[0] * N for _ in range(N)]
        q.append([i, j])
        visited = ''

