import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 돌의 수 / M: 뒤집기 횟수
    start_position = list(map(int, input().split()))    # 돌 초기 상태
    reverse_stone = [list(map(int, input().split())) for _ in range(M)]

    color_change = {1: 0, 0: 1}

    for a in range(M):
        i = reverse_stone[a][0] - 1    # 기준 돌의 인덱스
        j = reverse_stone[a][1]    # 마주보는 돌의 갯수

        for k in range(1, j+1):
            if 0 <= i - k and i + k < N:
                if start_position[i-k] == start_position[i+k]:
                    start_position[i - k] = color_change[start_position[i - k]]
                    start_position[i + k] = color_change[start_position[i + k]]
                else:
                    continue

    print(f'#{tc}', *start_position)

