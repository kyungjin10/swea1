import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    flower_max = 0

    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
                for c in range(1, 2):
                    ni, nj = i + di*c, j + dj*c
                    if 0 <= ni < N and 0 <= nj < M:
                        s += arr[ni][nj]
                if flower_max < s:
                    flower_max = s

    print(f'#{tc} {flower_max}')
