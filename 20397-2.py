import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    start_position = list(map(int, input().split()))
    change_order = [list(map(int, input().split())) for _ in range(M)]

    change_color = {1:0, 0:1}

    for k in range(M):
        i = change_order[k][0] - 1
        j = change_order[k][1]

        for a in range(1, j+1):
            if 0 <= i-a < N and 0 <= i+a < N:
                if start_position[i-a] == start_position[i+a]:
                    start_position[i-a] = change_color[start_position[i-a]]
                    start_position[i+a] = change_color[start_position[i+a]]

    print(f'#{tc}', *start_position)