import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    start_position = list(map(int, input().split()))
    reverse_stone = [list(map(int, input().split())) for _ in range(M)]

    #print(start_position[0])


    for a in range(M):
        i = reverse_stone[a][0] - 1     # 시작 인덱스
        j = reverse_stone[a][1]         # 바꿀 돌 개수

        new_color = start_position[i]
        for k in range(j):
            if i + k < N:
                start_position[i + k] = new_color

    print(f'#{tc}', *start_position)