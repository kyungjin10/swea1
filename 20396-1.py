import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    start_position = list(map(int, input().split()))
    change_order = [list(map(int, input().split())) for _ in range(M)]

    for k in range(M):
        i = change_order[k][0] - 1
        j = change_order[k][1]

        start_color = start_position[i]
        for a in range(j):
            if i + a < N:
                start_position[i+a] = start_color

    print(f'#{tc}', *start_position)

